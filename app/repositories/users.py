#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uuid

from app.models import User
from app.weblib.db import expunged


class UsersRepository(object):
    @staticmethod
    def get(id):
        return expunged(User.query.filter(User.id == id).first(),
                        User.session)

    @staticmethod
    def add(facebook_id, name, avatar, token):
        user = User(id=facebook_id, name=name, avatar=avatar, token=token)
        return user

    @staticmethod
    def authorized_by(token):
        return expunged(User.query.filter(User.token == token).first(),
                        User.session)
