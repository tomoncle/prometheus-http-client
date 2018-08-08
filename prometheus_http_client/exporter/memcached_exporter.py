#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-8-8 下午8:16
# @Author         : Tom.Lee
# @File           : memcached_exporter.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 
from .exporter import Exporter
from ..prometheus import prom


class MemcachedExporter(Exporter):
    """
    memcached status info
    """

    @prom
    def memcached_commands_total(self, **kwargs):
        pass

    @prom
    def memcached_connections_total(self, **kwargs):
        pass

    @prom
    def memcached_current_bytes(self, **kwargs):
        pass

    @prom
    def memcached_current_connections(self, **kwargs):
        pass

    @prom
    def memcached_current_items(self, **kwargs):
        pass

    @prom
    def memcached_items_evicted_total(self, **kwargs):
        pass

    @prom
    def memcached_items_reclaimed_total(self, **kwargs):
        pass

    @prom
    def memcached_items_total(self, **kwargs):
        pass

    @prom
    def memcached_limit_bytes(self, **kwargs):
        pass

    @prom
    def memcached_malloced_bytes(self, **kwargs):
        pass

    @prom
    def memcached_max_connections(self, **kwargs):
        pass

    @prom
    def memcached_read_bytes_total(self, **kwargs):
        pass

    @prom
    def memcached_up(self, **kwargs):
        pass

    @prom
    def memcached_uptime_seconds(self, **kwargs):
        pass

    @prom
    def memcached_version(self, **kwargs):
        pass

    @prom
    def memcached_written_bytes_total(self, **kwargs):
        pass



