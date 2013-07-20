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
from app.weblib.utils import jsonify


class PartiesController(CookieAuthorizableController):
    @authorized
    def GET(self):
        return jsonify(parties=[{
            'id': 'id1',
            'photo': 'http://www.petfinder.com/wp-content/uploads/2012/11/101418789-cat-panleukopenia-fact-sheet-632x475.jpg',
            'name': 'Name 1'
        }, {
            'id': 'id2',
            'photo': 'http://www.catster.com/files/short-hair-cat-01-shutterstock_129341936.jpg',
            'name': 'Name 2'
        }])
