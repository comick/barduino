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
from app.weblib.request_decorators import authorized


class PartiesController(CookieAuthorizableController):
    @authorized
    def GET(self):
        pass

