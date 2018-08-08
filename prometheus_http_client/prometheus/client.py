#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-8-6 上午8:33
# @Author         : Tom.Lee
# @File           : client.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 
import json
import os
from functools import wraps

from ..provider import PrometheusError
from ..provider import check_params

try:
    import urllib3
except ImportError:
    try:
        from requests.packages import urllib3
    except ImportError:
        urllib3 = None

if urllib3:
    urllib3.disable_warnings()


class Prometheus(object):
    def __init__(self):
        self.url = os.getenv('PROMETHEUS_URL', 'http://localhost:9090')
        self.headers = os.getenv('PROMETHEUS_HEAD', None)
        if self.headers:
            self.headers = json.loads(self.headers)
        self.step_size = 257.142857143

    def get_step(self, start, end):
        # compute graph point size
        pass

    @check_params('metric')
    def query(self, **kwargs):
        # query last point
        # kwargs:
        #       metric: string
        #       time  : timestamp , default time.time()
        #
        # Prometheus().query(metric="node_cpu")
        # Prometheus().query(metric='sum by (mode, instance, job) (irate(node_cpu{job="static_nodes"}[5m]))')
        pass

    @check_params(['metric', 'start', 'end'])
    def query_rang(self, **kwargs):
        # query graph points
        # kwargs:
        #       metric: string
        #       start : timestamp
        #       end   : timestamp
        #       step  : int, s, m, h, d, w, y , default None
        #
        # Prometheus().query_rang(metric="node_cpu", start=1533645703.78, end=1533649303.78)
        pass

    def targets(self):
        # query targets
        #
        # Prometheus().targets()
        pass

    def series(self, matches):
        # Querying metadata
        #
        # Prometheus().series(['up','process_start_time_seconds{job="prometheus"}'])
        pass

    def label_values(self, label):
        # Querying label values
        #
        # Prometheus().label_values('job')
        pass

    def alert_managers(self):
        # Prometheus alertmanager discovery
        #
        # Prometheus().alert_managers()
        pass


def _ignore(*args):
    """
    ignore params
    :param args:
    :return: None
    """
    _ = args


def _build_params(dic):
    """
    build params {...}
    :param dic: dict
    :return:  str
    """
    s = ''
    if not dic:
        return s
    if not isinstance(dic, dict):
        raise AssertionError("params must be dict type.")
    for k, v in dic.items():
        if s:
            s += ', {}="{}"'.format(k, v)
        else:
            s = '{}="{}"'.format(k, v)
    return '{%s}' % s


def prom(func):
    """
    execute metric request

    :param func: exporter method
    :return: metric monitor data, json
    """

    def wrapper(*args, **kwargs):
        graph = kwargs.pop('graph', False)
        filters = kwargs.pop('filter', {})
        prometheus = Prometheus()
        kwargs['metric'] = func.__name__ + _build_params(filters)
        function = prometheus.query_rang if graph else prometheus.query
        try:
            _ignore(args)
            return function(**kwargs)
        except AssertionError:
            raise
        except Exception as e:
            raise PrometheusError(e)

    return wrapper


def relabel(name):
    """
    rename metric name

    :param name:
    :return: metric monitor data, json
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func.__name__ = name
            filters = kwargs.pop('filter', {})
            if '{mode="idle"}' in name and 'mode' not in filters.keys():
                filters['mode'] = 'idle'
            query = _build_params(filters)
            if query:
                func.__name__ = name.replace('{mode="idle"}', query).replace('{}', query)
            return prom(func)(*args, **kwargs)

        return wrapper

    return decorator
