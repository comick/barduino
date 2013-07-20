#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.controllers import IndexController


URLS = (
    '/', IndexController,
    #'/login', LoginController,
    #'/parties', PartiesController,
    #'/tubi', TubiController,
    #'/birrini', BirriniController,
    #'/start', StartController,
    #'/q', QueueController
)
