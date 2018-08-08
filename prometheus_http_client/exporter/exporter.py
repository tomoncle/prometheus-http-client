#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-8-7 下午4:03
# @Author         : Tom.Lee
# @File           : exporter.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 
from ..prometheus import prom


class Exporter(object):
    """
    prometheus exporter

    examples:
        Exporter().go_gc_duration_seconds(filter={'instance':'127.0.0.1:9100'})
        Exporter().go_gc_duration_seconds(graph=True,filter={'instance':'127.0.0.1:9100'}, start=1533615123.5, end=1533615773.5)

    kwargs:
           graph:          True/False                                        default False
           start:          timestamp
           end:            timestamp
           step:           int (graph point step size)                       default None
           time:           timestamp                                         default time.time()
           filter:         {'instance':'127.0.0.1', 'label':'go lang', ...}
    :return: json
    """

    @prom
    def go_gc_duration_seconds(self, **kwargs):
        pass

    @prom
    def go_gc_duration_seconds_count(self, **kwargs):
        pass

    @prom
    def go_gc_duration_seconds_sum(self, **kwargs):
        pass

    @prom
    def go_goroutines(self, **kwargs):
        pass

    @prom
    def go_info(self, **kwargs):
        pass

    @prom
    def go_memstats_alloc_bytes(self, **kwargs):
        pass

    @prom
    def go_memstats_alloc_bytes_total(self, **kwargs):
        pass

    @prom
    def go_memstats_buck_hash_sys_bytes(self, **kwargs):
        pass

    @prom
    def go_memstats_frees_total(self, **kwargs):
        pass

    @prom
    def go_memstats_gc_cpu_fraction(self, **kwargs):
        pass

    @prom
    def go_memstats_gc_sys_bytes(self, **kwargs):
        pass

    @prom
    def go_memstats_heap_alloc_bytes(self, **kwargs):
        pass

    @prom
    def go_memstats_heap_idle_bytes(self, **kwargs):
        pass

    @prom
    def go_memstats_heap_inuse_bytes(self, **kwargs):
        pass

    @prom
    def go_memstats_heap_objects(self, **kwargs):
        pass

    @prom
    def go_memstats_heap_released_bytes(self, **kwargs):
        pass

    @prom
    def go_memstats_heap_sys_bytes(self, **kwargs):
        pass

    @prom
    def go_memstats_last_gc_time_seconds(self, **kwargs):
        pass

    @prom
    def go_memstats_lookups_total(self, **kwargs):
        pass

    @prom
    def go_memstats_mallocs_total(self, **kwargs):
        pass

    @prom
    def go_memstats_mcache_inuse_bytes(self, **kwargs):
        pass

    @prom
    def go_memstats_mcache_sys_bytes(self, **kwargs):
        pass

    @prom
    def go_memstats_mspan_inuse_bytes(self, **kwargs):
        pass

    @prom
    def go_memstats_mspan_sys_bytes(self, **kwargs):
        pass

    @prom
    def go_memstats_next_gc_bytes(self, **kwargs):
        pass

    @prom
    def go_memstats_other_sys_bytes(self, **kwargs):
        pass

    @prom
    def go_memstats_stack_inuse_bytes(self, **kwargs):
        pass

    @prom
    def go_memstats_stack_sys_bytes(self, **kwargs):
        pass

    @prom
    def go_memstats_sys_bytes(self, **kwargs):
        pass

    @prom
    def go_threads(self, **kwargs):
        pass

    @prom
    def http_request_duration_microseconds(self, **kwargs):
        pass

    @prom
    def http_request_duration_microseconds_count(self, **kwargs):
        pass

    @prom
    def http_request_duration_microseconds_sum(self, **kwargs):
        pass

    @prom
    def http_request_size_bytes(self, **kwargs):
        pass

    @prom
    def http_request_size_bytes_count(self, **kwargs):
        pass

    @prom
    def http_request_size_bytes_sum(self, **kwargs):
        pass

    @prom
    def http_requests_total(self, **kwargs):
        pass

    @prom
    def http_response_size_bytes(self, **kwargs):
        pass

    @prom
    def http_response_size_bytes_count(self, **kwargs):
        pass

    @prom
    def http_response_size_bytes_sum(self, **kwargs):
        pass
