#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import random
from datetime import timedelta
from datetime import datetime

import web

import app.config as config
from app.models import User
from app.controllers import CookieAuthorizableController
from app.repositories.users import UsersRepository


class LoginController():
    def GET(self):
        if 'fake_access_token' in web.ctx.session:
            raise web.found(web.ctx.path_url + '/authorized')

        web.ctx.session['fake_access_token'] = hashlib.sha256(
                str(datetime.now())).digest()
        raise web.found(web.ctx.path_url + '/authorized')


class LoginAuthorizedController(CookieAuthorizableController):
    def GET(self):
        id = 'fake_id'
        token = 'fake_token'
        user = UsersRepository.authorized_by(token)
        if user is None:
            user = UsersRepository.add('fake_id', 'fake_token')
            web.ctx.orm.add(user)
            web.ctx.orm.commit()
            # Merge fying and persistent object: this enables us to read the
            # automatically generated user id
            user = web.ctx.orm.merge(user)

        web.setcookie('token', user.token)

        raise web.found('/settings/parties')
