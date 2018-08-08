#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-8-7 下午8:40
# @Author         : Tom.Lee
# @File           : core.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 


def check_params(params):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if isinstance(params, str):
                if not kwargs.get(params, None):
                    raise AssertionError('parameter "{}" is necessary.'.format(params))
            elif isinstance(params, list):
                for param in params:
                    if not kwargs.get(param, None):
                        raise AssertionError('parameter "{}" is necessary.'.format(params))
            else:
                raise AssertionError('parameter "{}" is necessary.'.format(params))
            return func(*args, **kwargs)

        return wrapper

    return decorator


class PrometheusError(Exception):
    """
    Prometheus http error
    """
