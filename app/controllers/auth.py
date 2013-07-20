#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import json
import random
import urllib
import urlparse
from datetime import timedelta
from datetime import datetime

import oauth2
import web

import app.config as config
from app.models import User
from app.controllers import CookieAuthorizableController
from app.repositories.users import UsersRepository


AUTHORIZE_URL = 'https://www.facebook.com/dialog/oauth'
ACCESS_TOKEN_URL = 'https://graph.facebook.com/oauth/access_token'


class LoginController():
    def GET(self):
        if 'facebook_access_token' in web.ctx.session:
            raise web.found(web.ctx.path_url + '/authorized')

        data = web.input(error=None, code=None)

        if data.error:
            # The client denied permissions to the app
            # XXX flash some message here
            raise web.found('/')

        if data.code is None:
            raise web.found(AUTHORIZE_URL + '?' + urllib.urlencode(
                dict(client_id=web.config.FACEBOOK_APP_ID,
                     redirect_uri=web.ctx.path_url,
                     response_type='code',
                     scope='user_events')))

        consumer = oauth2.Consumer(web.config.FACEBOOK_APP_ID,
                                   web.config.FACEBOOK_APP_SECRET)
        client = oauth2.Client(consumer)
        (resp, content) = client.request(ACCESS_TOKEN_URL + '?'
                + urllib.urlencode(dict(code=data.code,
                                        client_id=web.config.FACEBOOK_APP_ID,
                                        client_secret=web.config.FACEBOOK_APP_SECRET,
                                        redirect_uri=web.ctx.path_url)), 'GET')
        if resp['status'] != '200':
            # XXX flash some message here
            web.debug(content)
            raise web.found('/')

        access_token = urlparse.parse_qs(content)
        web.ctx.session['facebook_access_token'] = access_token
        raise web.found(web.ctx.path_url + '/authorized')


class LoginAuthorizedController(CookieAuthorizableController):
    def GET(self):
        if 'facebook_access_token' not in web.ctx.session:
            raise web.found('/')

        access_token = web.ctx.session.pop('facebook_access_token')
        access_token = access_token['access_token'][-1]
        profile = json.load(
                urllib.urlopen(
                    "https://graph.facebook.com/me?" +
                    urllib.urlencode(dict(access_token=access_token))))

        user = UsersRepository.get(profile['id'])
        if not user:
            user = UsersRepository.add(profile['id'], access_token)
        user.token = access_token

        web.ctx.orm.add(user)
        web.ctx.orm.commit()
        # Merge fying and persistent object: this enables us to read the
        # automatically generated user id
        user = web.ctx.orm.merge(user)

        web.setcookie('token', user.token)

        raise web.found('/settings/parties')
