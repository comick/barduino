#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web

from app.controllers import CookieAuthorizableController
from app.weblib.request_decorators import authorized
from app.weblib.utils import jsonify


class TubiController(CookieAuthorizableController):
    @authorized
    def GET(self):
        return jsonify(tubi=[{
            'id': 0,
            'event_id': 'id1',
            'bibendus': 'Gin',
        }, {
            'id': 1,
            'event_id': 'id1',
            'bibendus': 'Aperol',
        }, {
            'id': 2,
            'event_id': 'id1',
            'bibendus': 'Campari',
        }, {
            'id': 3,
            'event_id': 'id1',
            'bibendus': 'Red-bull',
        }])
