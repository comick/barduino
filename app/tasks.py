#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import time
import urllib

from app.config import DRINKS
from app.celery import celery
from app.repositories.requests import RequestsRepository
from app.weblib.db import create_session


def generate_message(pending):
    if not pending:
        return 'No pending requests! '\
               'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQfQs6py2RHKlPNUumcG20b5zGYIyH3tAfMJk6l-EArqQs2iFGv'
    message = '%(pending)s pending requests! '\
              'http://clipartist.info/RSS/png/y_u_no_guy_y_u_no-1331px.png'
    return message % dict(pending=pending)


def process_comment(access_token, party_id, post, pending):
    for drink in DRINKS:
        if drink[0].lower() in post['message']:
            # Comment
            comment_id = post['id']
            resp = json.load(
                    urllib.urlopen(
                        'https://graph.facebok.com/' + comment_id + '/comments',
                        urllib.urlencode(dict(message=generate_message(pending),
                                              access_token=access_token))))
            # Add new request
            return RequestsRepository.add(party_id, post['id'],
                                          post['from']['id'],
                                          post['from']['name'],
                                          post['message'], drink[0])


@celery.task
def PollPartyTask(user):
    access_token = user.token
    party_id = user.party_id
    since = 0
    while True:
        session = create_session()
        resp = json.load(
                urllib.urlopen(
                    'https://graph.facebok.com/' + party_id + '/feed?' +
                    urllib.urlencode(dict(fields='comments,message,from',
                                        date_format='U',
                                        since=since,
                                        access_token=access_token))))
        posts = [p for p in resp['data']]
        comments = [p for p in posts if 'message' in p]

        pending = len(RequestsRepository.pending())
        requests_to_add = []
        for c in comments:
            r = process_comment(access_token, party_id, c, pending)
            if r is not None:
                requests_to_add.append(r)
                pending += 1
        session.add_all(requests_to_add)
        session.commit()

        [MakeBirroTask.delay(access_token, r.id) for r in requests_to_add]

        # Reschedule next execution
        time.sleep(10)
        since = posts[0]['created_time'] if posts else since


@celery.task
def MakeBirroTask(access_token, request_id):
    session = create_session()
    request = RequestsRepository.get(request_id)
    resp = json.load(
            urllib.urlopen(
                'https://graph.facebok.com/' + request.comment_id + '/comments',
                urllib.urlencode(dict(message='Come here!',
                    access_token=access_token))))
    request.served = True
    session.add(request)
    session.commit()
