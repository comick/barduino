#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web

from app.controllers import CookieAuthorizableController
from app.weblib.request_decorators import authorized
from app.weblib.utils import jsonify


class DrinksController(CookieAuthorizableController):
    @authorized
    def GET(self):
        return jsonify(drinks=[{
            'name': 'Gin Tonic',
            'recipe': [{
                'index': 0,
                'percentage': 33
            }]
        }])

