#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib

import web

from app.repositories.requests import RequestsRepository
from app.controllers import CookieAuthorizableController
from app.weblib.request_decorators import authorized
from app.weblib.utils import jsonify


def parse_comment(access_token, request):
    resp = json.load(
            urllib.urlopen(
                'https://graph.facebook.com/' + request.comment_id + '?' +
                urllib.urlencode(dict(access_token=access_token))))
    profile = json.load(
            urllib.urlopen(
                'https://graph.facebook.com/' + resp['from']['id'] + '?' +
                urllib.urlencode(dict(access_token=access_token))))
    return {
        'name': resp['from']['name'],
        'avatar': 'https://graph.facebook.com/%(id)s/picture?type=large' % dict(id=resp['from']['id']),
        'message': resp['message'],
    }


class RequestsController(CookieAuthorizableController):
    @authorized
    def GET(self):
        return jsonify(requests=[parse_comment(self.current_user.token, r)
                                 for r in RequestsRepository.pending()])
