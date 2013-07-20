#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib
import web

from app.controllers import CookieAuthorizableController
from app.weblib.request_decorators import authorized
from app.weblib.utils import jsonify


class PartiesController(CookieAuthorizableController):
    @authorized
    def GET(self):
        access_token = self.current_user.token
        resp = json.load(
                urllib.urlopen(
                    'https://graph.facebook.com/me?' +
                    urllib.urlencode(dict(fields='events.fields(name,cover)',
                                          access_token=access_token))))
        return jsonify(parties=[{
            'id': e['id'],
            'name': e['name'],
            'photo': e['cover']['source'] if 'cover' in e else None
        } for e in resp['events']['data']])


class SelectPartyController(CookieAuthorizableController):
    @authorized
    def GET(self):
        user = self.current_user
        user.party_id = web.input(party_id=None).party_id

        web.ctx.orm.add(user)
        web.ctx.orm.commit()
        raise web.found('/settings/tubi')
