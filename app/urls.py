#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.controllers import IndexController
from app.controllers import SettingsPartiesController
from app.controllers.auth import LoginController
from app.controllers.auth import LoginAuthorizedController
from app.controllers.parties  import PartiesController
from app.controllers.parties  import SelectPartyController


URLS = (
    '/', IndexController,
    '/login', LoginController,
    '/login/authorized', LoginAuthorizedController,
    '/settings/parties', SettingsPartiesController,
    '/parties', PartiesController,
    '/parties/select', SelectPartyController
    #'/parties', PartiesController,
    #'/tubi', TubiController,
    #'/birrini', BirriniController,
    #'/start', StartController,
    #'/q', QueueController
)
