#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.controllers import IndexController
from app.controllers.auth import LoginController
from app.controllers.auth import LoginAuthorizedController
from app.controllers.parties  import PartiesController


URLS = (
    '/', IndexController,
    '/login', LoginController,
    '/login/authorized', LoginAuthorizedController,
    '/parties', PartiesController,
    #'/parties', PartiesController,
    #'/tubi', TubiController,
    #'/birrini', BirriniController,
    #'/start', StartController,
    #'/q', QueueController
)
