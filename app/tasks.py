#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import time
import urllib

from app.config import DRINKS
from app.celery import celery


def process_comment(comment):
    for drink in DRINKS:
        if drink[0].lower() in comment['message']:
            raise ValueError(drink)
    return comment


@celery.task
def PollPartyTask(user, since=0):
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

    [process_comment(c) for c in comments]

    # Reschedule next execution
    time.sleep(5)
    PollPartyTask.delay(user, posts[0]['created_time'] if posts else since)
