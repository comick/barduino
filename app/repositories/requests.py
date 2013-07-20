#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.models import Request
from app.weblib.db import expunged
from app.weblib.db import uuid


class RequestsRepository(object):
    @staticmethod
    def pending():
        return [expunged(r, Request.session)
                for r in Request.query.filter(Request.served == False)\
                        .order_by(Request.created.desc()).all()]

    @staticmethod
    def add(party_id, comment_id, birro):
        id = uuid()
        request = Request(id=id, party_id=party_id,
                          comment_id=comment_id, birro=birro, served=False)
        return request
