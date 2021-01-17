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

def _golang_parsebool(string):
        if string in {'1', 't', 'T', 'TRUE', 'true', 'True'}:
            return True
        if string in {'0', 'f', 'F', 'FALSE', 'false', 'False'}:
            return False
        raise ValueError('could not parse boolean')

class Prometheus(object):
    def __init__(self, url=None, headers=None, verify_ssl=None,
                 certs=None, timeout=None):
        self.url = url or os.getenv('PROMETHEUS_URL', 'http://localhost:9090')
        if headers:
            self.headers = headers
        else:
            self.headers = os.getenv('PROMETHEUS_HEAD', None)
            if self.headers:
                self.headers = json.loads(self.headers)

        self.timeout = float(os.getenv('PROMETHEUS_TIMEOUT', timeout))

        self.step_size = 257.142857143

        if verify_ssl is not None:
            self.verify_ssl = verify_ssl
        elif (
            "PROMETHEUS_VERIFY_SSL" in os.environ
            and _golang_parsebool(os.environ['PROMETHEUS_VERIFY_SSL']) is False
        ):
            self.verify_ssl = False
        elif "PROMETHEUS_CA_BUNDLE" in os.environ:
            self.verify_ssl = os.environ['PROMETHEUS_CA_BUNDLE']
        else:
            self.verify_ssl = True

        self.certs = certs

        if (os.getenv('PROMETHEUS_CERT', None)
            and os.getenv('PROMETHEUS_KEY', None)):
            self.certs = (os.getenv('PROMETHEUS_CERT', None),
                os.getenv('PROMETHEUS_KEY', None))


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

    def rules(self, **kwargs):
        # Querying the rules
        #
        # Prometheus().rules(type="alert")
        # type: alert|record
        pass

    def alerts(self):
        # Queriying for active alerts
        #
        # Prometheus().alerts()
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
    Examples:
        {"bar":"foo", "lab":"this"} --> {bar="foo", lab="this"}
        {"bar":("!=",foo",), "lab":"this"} --> {bar!="foo", lab="this"}
    """
    s = ''
    if not dic:
        return s
    if not isinstance(dic, dict):
        raise AssertionError("params must be dict type.")
    for k, v in dic.items():
        # if the value is a tuple then the caller likes to give also the operator like !=, =~ and so on.
        # else the caller just likes label equals value filter
        if isinstance(v, tuple):
            s += '{}{}"{}", '.format(k, v[0], v[1])
        else:
            s += '{}="{}", '.format(k, v)
    # remove last comma
    s = str(s[:-2])
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
