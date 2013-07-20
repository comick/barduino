#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib

from app.celery import celery


def process_comment(comment):
    return comment


@celery.task
def PollPartyTask(user):
    #access_token = self.current_user.token XXX
    access_token = 'CAAFgztesdO8BAMSIUjvmW0aewKp1ZBHPEtT95Rfe1it1DMTR1OzORZB9LOusFVHWx1aHStBMv7cwBwEf2cHPAuU2b4BNywJQsm0gTEUZC21jvkxiO3L4Tr07HcbkNIZCBIS7J3DUBh3RF6E7R2spyuwisTEXPSAZD'
    #party_id = self.current_user.party_id XXX
    party_id = '417578625021950'
    resp = json.load(
            urllib.urlopen(
                'https://graph.facebok.com/' + party_id + '/feed?' +
                urllib.urlencode(dict(access_token=access_token))))

    raise ValueError([process_comment(c) for c in resp['data']
                                         if 'message' in c])
