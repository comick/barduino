#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web

from app.config import TUBI
from app.controllers import CookieAuthorizableController
from app.weblib.request_decorators import authorized
from app.weblib.utils import jsonify


class TubiController(CookieAuthorizableController):
    @authorized
    def GET(self):
        return jsonify(tubi=[{
            'index': t[0],
            'bibendus': t[1]
        } for t in TUBI])
