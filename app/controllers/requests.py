#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib

import web

from app.repositories.requests import RequestsRepository
from app.controllers import CookieAuthorizableController
from app.weblib.request_decorators import authorized
from app.weblib.utils import jsonify


class RequestsController(CookieAuthorizableController):
    @authorized
    def GET(self):
        return jsonify(requests=[{
            'birro': r.birro,
            'name': r.from_name,
            'avatar': 'https://graph.facebook.com/%(id)s/picture?type=large' % dict(id=r.from_id),
            'message': r.message
        } for r in RequestsRepository.pending(self.current_user.party_id)])
