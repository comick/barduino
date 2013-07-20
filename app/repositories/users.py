#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uuid

from app.models import User
from app.weblib.db import expunged


class UsersRepository(object):
    @staticmethod
    def get(id):
        return expunged(User.query.options(joinedload('driver'),
                                           joinedload('passenger')).\
                                filter(User.deleted == False).\
                                filter(User.id == id).first(),
                        User.session)

    @staticmethod
    def add(facebook_id, facebook_token):
        id = unicode(uuid.uuid4())
        user = User(id=id, facebook_id=facebook_id,
                    facebook_token=facebook_token)
        return user

    @staticmethod
    def authorized_by(token):
        return expunged(User.query.filter(User.facebook_token == token).first(),
                        User.session)
