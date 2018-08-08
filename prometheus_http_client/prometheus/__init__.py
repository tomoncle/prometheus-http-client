#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-8-6 上午7:44
# @Author         : Tom.Lee
# @File           : __init__.py.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 

from .client import Prometheus
from .client import prom
from .client import relabel
from ..provider import load_init

load_init(Prometheus)
__all__ = [
    'Prometheus',
    'prom',
    'relabel'
]
