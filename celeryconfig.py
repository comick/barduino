#!/usr/bin/env python
# -*- coding: utf-8 -*-

from celery.schedules import crontab

CELERY_IMPORTS = ('app.tasks',)

BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
