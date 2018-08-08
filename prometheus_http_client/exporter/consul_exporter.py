#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-8-8 下午8:25
# @Author         : Tom.Lee
# @File           : consul_exporter.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 
from .exporter import Exporter
from ..prometheus import prom
from ..prometheus import relabel


class ConsulExporter(Exporter):
    """
    consul status info
    """

    @prom
    def consul_catalog_service_node_healthy(self, **kwargs):
        pass

    @prom
    def consul_catalog_services(self, **kwargs):
        pass

    @prom
    def consul_exporter_build_info(self, **kwargs):
        pass

    @prom
    def consul_health_node_status(self, **kwargs):
        pass

    @prom
    def consul_raft_leader(self, **kwargs):
        pass

    @prom
    def consul_raft_peers(self, **kwargs):
        pass

    @prom
    def consul_serf_lan_members(self, **kwargs):
        pass

    @prom
    def consul_up(self, **kwargs):
        pass

    @relabel('min(consul_catalog_service_node_healthy) by (service_name)')
    def consul_services_healthy(self, **kwargs):
        # Values of 1 mean that all nodes for the service are passing.
        # Values of 0 mean at least one node for the service is not passing.
        pass

    @relabel('sum by (node, service_name)(consul_catalog_service_node_healthy == 0)')
    def consul_service_nodes_failing(self, **kwargs):
        pass

    @relabel('consul_health_service_status{status="critical"} == 1')
    def consul_service_checks_critical(self, **kwargs):
        # You can query for the following health check states:
        # "maintenance", "critical", "warning" or "passing"
        pass
