#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web

from app.repositories.users import UsersRepository
from app.weblib.request_decorators import api
from app.weblib.controllers import AbstractCookieAuthorizableController
from app.weblib.controllers import AbstractParamAuthorizableController


class CookieAuthorizableController(AbstractCookieAuthorizableController):
    def get_user(self, token):
        return UsersRepository.authorized_by(token)


class ParamAuthorizableController(AbstractParamAuthorizableController):
    def get_user(self, token):
        return UsersRepository.authorized_by(token)


class IndexController(ParamAuthorizableController):
    def GET(self):
        return web.ctx.render.index()


class SettingsPartiesController(ParamAuthorizableController):
    def GET(self):
        return web.ctx.render.parties()
