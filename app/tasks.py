#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import time
import urllib

from app.config import DRINKS
from app.celery import celery
from app.repositories.requests import RequestsRepository
from app.weblib.db import create_session


def process_comment(access_token, party_id, comment, added):
    for drink in DRINKS:
        if drink[0].lower() in comment['message']:
            # Comment
            comment_id = comment['id']
            message = 'Cristo! (%(pending)s pending requests!)'
            pending = len(RequestsRepository.pending()) + added
            message = message % dict(pending=pending)
            resp = json.load(
                    urllib.urlopen(
                        'https://graph.facebok.com/' + comment_id + '/comments',
                        urllib.urlencode(dict(message=message,
                                              access_token=access_token))))
            # Add new request
            return RequestsRepository.add(party_id, comment['id'])


@celery.task
def PollPartyTask(user, since=0):
    session = create_session()
    #access_token = self.current_user.token XXX
    access_token = 'CAAFgztesdO8BAMSIUjvmW0aewKp1ZBHPEtT95Rfe1it1DMTR1OzORZB9LOusFVHWx1aHStBMv7cwBwEf2cHPAuU2b4BNywJQsm0gTEUZC21jvkxiO3L4Tr07HcbkNIZCBIS7J3DUBh3RF6E7R2spyuwisTEXPSAZD'
    #party_id = self.current_user.party_id XXX
    party_id = '417578625021950'
    resp = json.load(
            urllib.urlopen(
                'https://graph.facebok.com/' + party_id + '/feed?' +
                urllib.urlencode(dict(fields='comments,message',
                                      date_format='U',
                                      since=since,
                                      access_token=access_token))))
    posts = [p for p in resp['data']]
    comments = [p for p in posts if 'message' in p]

    added = 0
    for c in comments:
        r = process_comment(access_token, party_id, c, added)
        if r is not None:
            session.add(r)
            added += 1
    session.commit()

    # Reschedule next execution
    time.sleep(5)
    PollPartyTask.delay(user, posts[0]['created_time'] if posts else since)
