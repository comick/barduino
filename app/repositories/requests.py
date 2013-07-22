#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.models import Request
from app.weblib.db import expunged
from app.weblib.db import uuid


class RequestsRepository(object):
    @staticmethod
    def get(id):
        return expunged(Request.query.filter(Request.id == id).first(),
                        Request.session)

    @staticmethod
    def pending(party_id):
        return [expunged(r, Request.session)
                for r in Request.query\
                        .filter(Request.party_id == party_id)\
                        .filter(Request.served == False)\
                        .order_by(Request.created.desc()).all()]

    @staticmethod
    def add(party_id, comment_id, from_id, from_name, message, birro):
        id = uuid()
        request = Request(id=id, party_id=party_id, comment_id=comment_id,
                          from_id=from_id, from_name=from_name, message=message,
                          birro=birro, served=False)
        return request
