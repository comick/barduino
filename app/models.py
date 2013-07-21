#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

from weblib.db import backref
from weblib.db import declarative_base
from weblib.db import relationship
from weblib.db import uuid
from weblib.db import Boolean
from weblib.db import Column
from weblib.db import DateTime
from weblib.db import Enum
from weblib.db import ForeignKey
from weblib.db import Integer
from weblib.db import String
from weblib.db import Text
from weblib.db import Time



Base = declarative_base()


class Session(Base):
    __tablename__ = 'session'

    session_id = Column(String, primary_key=True)
    atime = Column(Time, default=datetime.now)
    data = Column(Text)


class User(Base):
    __tablename__ = 'user'

    id = Column(String, default=uuid, primary_key=True)
    name = Column(String)
    avatar = Column(String)
    token = Column(String)
    party_id = Column(String)


class Request(Base):
    __tablename__ = 'request'

    id = Column(String, default=uuid, primary_key=True)
    party_id = Column(String)
    comment_id = Column(String)
    from_id = Column(String)
    from_name = Column(String)
    message = Column(String)
    birro = Column(String)
    served = Column(Boolean)
    created = Column(DateTime, default=datetime.now)
