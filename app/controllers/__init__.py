#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web

from app.repositories.users import UsersRepository
from app.tasks import PollPartyTask
from app.weblib.controllers import AbstractCookieAuthorizableController
from app.weblib.controllers import AbstractParamAuthorizableController
from app.weblib.request_decorators import api
from app.weblib.request_decorators import authorized


class CookieAuthorizableController(AbstractCookieAuthorizableController):
    def get_user(self, token):
        return UsersRepository.authorized_by(token)


class IndexController(CookieAuthorizableController):
    def GET(self):
        return web.ctx.render.index()


class SettingsPartiesController(CookieAuthorizableController):
    @authorized
    def GET(self):
        return web.ctx.render.parties()


class SettingsTubiController(CookieAuthorizableController):
    @authorized
    def GET(self):
        return web.ctx.render.tubi()


class StartController(CookieAuthorizableController):
    @authorized
    def GET(self):
        PollPartyTask.delay(self.current_user)
        raise web.found('/q')


class QController(CookieAuthorizableController):
    @authorized
    def GET(self):
        return web.ctx.render.q()
