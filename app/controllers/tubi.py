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
            'index': 0,
            'bibendus': 'Gin',
        }, {
            'index': 1,
            'bibendus': 'Aperol',
        }, {
            'index': 2,
            'bibendus': 'Campari',
        }, {
            'index': 3,
            'bibendus': 'Red-bull',
        }])
