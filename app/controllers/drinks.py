#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web

from app.config import DRINKS
from app.controllers import CookieAuthorizableController
from app.weblib.request_decorators import authorized
from app.weblib.utils import jsonify


class DrinksController(CookieAuthorizableController):
    @authorized
    def GET(self):
        return jsonify(drinks=[{
            'name': t[0],
            'percentages': t[1]
        } for t in DRINKS])
