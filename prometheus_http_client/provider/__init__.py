#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-8-7 下午3:48
# @Author         : Tom.Lee
# @File           : __init__.py.py
# @Product        : PyCharm
# @Docs           : 
# @Source         :
import time

import requests

from .core import PrometheusError
from .core import check_params

__all__ = ['PrometheusError', 'check_params']

try:
    import urllib3
except ImportError:
    try:
        from requests.packages import urllib3
    except ImportError:
        urllib3 = None

if urllib3:
    urllib3.disable_warnings()


def _step(self, start, end):
    if start > end:
        raise AssertionError('start must be less than end timestamp.')
    step = (end - start) / self.step_size
    return 1 if step < 1 else int(step)


@check_params('metric')
def _q(self, **kwargs):
    return requests.get(
        url=self.url.rstrip('/') + '/api/v1/query',
        params={'query': kwargs.get('metric'), 'time': kwargs.get('time', time.time())},
        headers=self.headers).text


@check_params(['metric', 'start', 'end'])
def _qr(self, **kwargs):
    return requests.get(
        url=self.url.rstrip('/') + '/api/v1/query_range',
        params={
            'query': kwargs.get('metric'),
            'start': kwargs.get('start'),
            'end': kwargs.get('end'),
            'step': kwargs.get('step', self.get_step(kwargs.get('start'), kwargs.get('end')))},
        headers=self.headers).text


def _t(self):
    return requests.get(url=self.url.rstrip('/') + '/api/v1/targets', headers=self.headers).text


def _s(self, matches):
    url = self.url.rstrip('/') + '/api/v1/series'
    if matches:
        url += '?'
        for i, m in enumerate(matches):
            if i > 0:
                url += '&'
            url += 'match[]={}'.format(m)
    return requests.get(url=url, headers=self.headers).text


def _am(self):
    return requests.get(
        url=self.url.rstrip('/') + '/api/v1/alertmanagers',
        headers=self.headers).text


def _lv(self, label):
    return requests.get(
        url=self.url.rstrip('/') + '/api/v1/label/{}/values'.format(label),
        headers=self.headers).text


_dic = {
    'get_step': _step,
    'query': _q,
    'query_rang': _qr,
    'targets': _t,
    'series': _s,
    'alert_managers': _am,
    'label_values': _lv
}


def load_init(obj):
    for k, v in _dic.items():
        setattr(obj, k, v)
