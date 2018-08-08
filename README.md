# Prometheus-http-client [![Build Status](https://travis-ci.org/tomoncle/prometheus-http-client.svg?branch=master)][travis]
> Prometheus service http client

* More simple expansion: use wrapper Automatic selection query mode, there is no need for any implementation.
  ```python
  @prom
  def go_gc_duration_seconds(self, **kwargs):
      pass

  @prom
  def go_gc_duration_seconds_count(self, **kwargs):
      pass

  ```

* Custom query expression: there is no need for any implementation.
  ```python
  @relabel('100 - (avg by (instance, job) (irate(node_cpu{mode="idle"}[5m])) * 100)')
  def node_cpu_rate(self, **kwargs):
        pass

  @relabel(
        '(node_filesystem_size{} - node_filesystem_free{})'
        ' / (node_filesystem_size{} - node_filesystem_free{} + node_filesystem_avail{})'
        ' * 100')
  def node_disk_rate(self, **kwargs):
      pass
  ```

* Rich query selector: Support multi label query.
  ```python
  from prometheus_http_client import NodeExporter

  # default metric
  node_exporter = NodeExporter()

  # instance = 127.0.0.1:9100
  # job = static
  # mode = user
  print(node_exporter.node_cpu_rate(filter={'instance': '127.0.0.1:9100','mode':'user','job':'static'}))
  ```


## Install
* source:
```shell
$ git clone https://github.com/tomoncle/prometheus-http-client.git
$ cd prometheus-http-client && sudo python setup.py install
```

* pip: `$ pip install prometheus-http-client`

## Config
* default config : 'http://localhost:9090'

* change config  :
  ```bash
  $ export PROMETHEUS_URL='http://192.168.1.2:9090'
  ```

* auth config    :
  ```bash
  $ export PROMETHEUS_HEAD='{"Cookie": "123456"}'
  ```

## Query
### Prometheus
  ```python
  from prometheus_http_client import Prometheus


  # auto metric
  prometheus = Prometheus()
  # print(prometheus.query(metric='sum by (mode, instance,job) (irate(node_cpu{job="static_nodes"}[5m]))'))
  print(prometheus.query(metric='irate(node_cpu{job="static_nodes"}[5m])'))
  ```

* data :
  ```json
  {"status":"success","data":{"resultType":"vector","result":[{"metric":{"cpu":"cpu0","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"idle"},"value":[1533734649.92,"0.9706666666669965"]},{"metric":{"cpu":"cpu0","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"iowait"},"value":[1533734649.92,"0"]},{"metric":{"cpu":"cpu0","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"irq"},"value":[1533734649.92,"0"]},{"metric":{"cpu":"cpu0","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"nice"},"value":[1533734649.92,"0"]},{"metric":{"cpu":"cpu0","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"softirq"},"value":[1533734649.92,"0"]},{"metric":{"cpu":"cpu0","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"steal"},"value":[1533734649.92,"0"]},{"metric":{"cpu":"cpu0","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"system"},"value":[1533734649.92,"0.003999999999996362"]},{"metric":{"cpu":"cpu0","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"user"},"value":[1533734649.92,"0.012000000000004245"]},{"metric":{"cpu":"cpu1","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"idle"},"value":[1533734649.92,"0.981333333333411"]},{"metric":{"cpu":"cpu1","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"iowait"},"value":[1533734649.92,"0.0006666666666670077"]},{"metric":{"cpu":"cpu1","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"irq"},"value":[1533734649.92,"0"]},{"metric":{"cpu":"cpu1","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"nice"},"value":[1533734649.92,"0"]},{"metric":{"cpu":"cpu1","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"softirq"},"value":[1533734649.92,"0"]},{"metric":{"cpu":"cpu1","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"steal"},"value":[1533734649.92,"0"]},{"metric":{"cpu":"cpu1","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"system"},"value":[1533734649.92,"0.002666666666668031"]},{"metric":{"cpu":"cpu1","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"user"},"value":[1533734649.92,"0.009333333333324844"]},{"metric":{"cpu":"cpu2","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"idle"},"value":[1533734649.92,"0.971333333333314"]},{"metric":{"cpu":"cpu2","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"iowait"},"value":[1533734649.92,"0"]},{"metric":{"cpu":"cpu2","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"irq"},"value":[1533734649.92,"0"]},{"metric":{"cpu":"cpu2","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"nice"},"value":[1533734649.92,"0"]},{"metric":{"cpu":"cpu2","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"softirq"},"value":[1533734649.92,"0"]},{"metric":{"cpu":"cpu2","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"steal"},"value":[1533734649.92,"0"]},{"metric":{"cpu":"cpu2","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"system"},"value":[1533734649.92,"0.0033333333333303017"]},{"metric":{"cpu":"cpu2","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"user"},"value":[1533734649.92,"0.014666666666653328"]},{"metric":{"cpu":"cpu3","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"idle"},"value":[1533734649.92,"0.9253333333334013"]},{"metric":{"cpu":"cpu3","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"iowait"},"value":[1533734649.92,"0.047333333333333866"]},{"metric":{"cpu":"cpu3","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"irq"},"value":[1533734649.92,"0"]},{"metric":{"cpu":"cpu3","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"nice"},"value":[1533734649.92,"0"]},{"metric":{"cpu":"cpu3","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"softirq"},"value":[1533734649.92,"0"]},{"metric":{"cpu":"cpu3","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"steal"},"value":[1533734649.92,"0"]},{"metric":{"cpu":"cpu3","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"system"},"value":[1533734649.92,"0.0026666666666642414"]},{"metric":{"cpu":"cpu3","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"user"},"value":[1533734649.92,"0.031999999999986053"]}]}}
  ```

### Exporter
> Exporter for common metrics https://prometheus.io/

* code :
  ```python
  from prometheus_http_client import Exporter


  print(Exporter().go_gc_duration_seconds())
  ```

* data :
  ```json
  {"status":"success","data":{"resultType":"vector","result":[{"metric":{"__name__":"go_gc_duration_seconds","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","quantile":"0"},"value":[1533734495.25,"0.00002624"]},{"metric":{"__name__":"go_gc_duration_seconds","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","quantile":"0.25"},"value":[1533734495.25,"0.000048674"]},{"metric":{"__name__":"go_gc_duration_seconds","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","quantile":"0.5"},"value":[1533734495.25,"0.000064599"]},{"metric":{"__name__":"go_gc_duration_seconds","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","quantile":"0.75"},"value":[1533734495.25,"0.000084196"]},{"metric":{"__name__":"go_gc_duration_seconds","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","quantile":"1"},"value":[1533734495.25,"0.002391278"]},{"metric":{"__name__":"go_gc_duration_seconds","instance":"127.0.0.1:9104","job":"mysql","mysql_version":"5.7","quantile":"0"},"value":[1533734495.25,"0.000028267"]},{"metric":{"__name__":"go_gc_duration_seconds","instance":"127.0.0.1:9104","job":"mysql","mysql_version":"5.7","quantile":"0.25"},"value":[1533734495.25,"0.000040906"]},{"metric":{"__name__":"go_gc_duration_seconds","instance":"127.0.0.1:9104","job":"mysql","mysql_version":"5.7","quantile":"0.5"},"value":[1533734495.25,"0.00005304"]},{"metric":{"__name__":"go_gc_duration_seconds","instance":"127.0.0.1:9104","job":"mysql","mysql_version":"5.7","quantile":"0.75"},"value":[1533734495.25,"0.000093971"]},{"metric":{"__name__":"go_gc_duration_seconds","instance":"127.0.0.1:9104","job":"mysql","mysql_version":"5.7","quantile":"1"},"value":[1533734495.25,"0.004254732"]},{"metric":{"__name__":"go_gc_duration_seconds","instance":"127.0.0.1:9107","job":"consul","mysql_version":"5.7","quantile":"0"},"value":[1533734495.25,"0.00006202700000000001"]},{"metric":{"__name__":"go_gc_duration_seconds","instance":"127.0.0.1:9107","job":"consul","mysql_version":"5.7","quantile":"0.25"},"value":[1533734495.25,"0.000198266"]},{"metric":{"__name__":"go_gc_duration_seconds","instance":"127.0.0.1:9107","job":"consul","mysql_version":"5.7","quantile":"0.5"},"value":[1533734495.25,"0.00020824000000000003"]},{"metric":{"__name__":"go_gc_duration_seconds","instance":"127.0.0.1:9107","job":"consul","mysql_version":"5.7","quantile":"0.75"},"value":[1533734495.25,"0.000271729"]},{"metric":{"__name__":"go_gc_duration_seconds","instance":"127.0.0.1:9107","job":"consul","mysql_version":"5.7","quantile":"1"},"value":[1533734495.25,"0.001790822"]},{"metric":{"__name__":"go_gc_duration_seconds","instance":"127.0.0.1:9150","job":"memcached","mysql_version":"5.7","quantile":"0"},"value":[1533734495.25,"0.000025387"]},{"metric":{"__name__":"go_gc_duration_seconds","instance":"127.0.0.1:9150","job":"memcached","mysql_version":"5.7","quantile":"0.25"},"value":[1533734495.25,"0.000037497"]},{"metric":{"__name__":"go_gc_duration_seconds","instance":"127.0.0.1:9150","job":"memcached","mysql_version":"5.7","quantile":"0.5"},"value":[1533734495.25,"0.000060197"]},{"metric":{"__name__":"go_gc_duration_seconds","instance":"127.0.0.1:9150","job":"memcached","mysql_version":"5.7","quantile":"0.75"},"value":[1533734495.25,"0.000111523"]},{"metric":{"__name__":"go_gc_duration_seconds","instance":"127.0.0.1:9150","job":"memcached","mysql_version":"5.7","quantile":"1"},"value":[1533734495.25,"0.000544621"]}]}}
  ```

### node_exporter
> Exporter for machine metrics https://prometheus.io/
* code :
  ```python
  from prometheus_http_client import NodeExporter

  # default metric
  node_exporter = NodeExporter()

  # print(node_exporter.node_uname_info())
  print(node_exporter.node_cpu_rate(filter={'instance': '127.0.0.1:9100'}))
  ````

* data :
  ```json
  {"status":"success","data":{"resultType":"vector","result":[{"metric":{"instance":"127.0.0.1:9100","job":"static_nodes"},"value":[1533734848.099,"11.816666666676014"]}]}}
  ```

### mysqld_exporter
> Exporter for MySQL server metrics http://prometheus.io/

* code :
  ```python
  from prometheus_http_client import MysqlExporter

  print(MysqlExporter().mysql_exporter_scrapes_total())
  ````

* data :
  ```json
  {"status":"success","data":{"resultType":"vector","result":[{"metric":{"__name__":"mysql_exporter_scrapes_total","instance":"127.0.0.1:9104","job":"mysql","mysql_version":"5.7"},"value":[1533735043.46,"345"]}]}}
  ```

### consul_exporter
> Exporter for consul server metrics http://prometheus.io/

* code :
  ```python
  from prometheus_http_client import ConsulExporter

  print(ConsulExporter().consul_catalog_services())
  ````

* data :
  ```json
  {"status":"success","data":{"resultType":"vector","result":[{"metric":{"__name__":"consul_catalog_services","instance":"127.0.0.1:9107","job":"consul","mysql_version":"5.7"},"value":[1533735232.039,"1"]}]}}
  ```

### memcached_exporter
> Exporter for memcached server metrics http://prometheus.io/

* code :
  ```python
  from prometheus_http_client import MemcachedExporter

  print(MemcachedExporter().memcached_commands_total())
  ````

* data :
  ```json
  {"status":"success","data":{"resultType":"vector","result":[{"metric":{"__name__":"memcached_commands_total","command":"cas","instance":"127.0.0.1:9150","job":"memcached","mysql_version":"5.7","status":"badval"},"value":[1533735286.809,"0"]},{"metric":{"__name__":"memcached_commands_total","command":"cas","instance":"127.0.0.1:9150","job":"memcached","mysql_version":"5.7","status":"hit"},"value":[1533735286.809,"0"]},{"metric":{"__name__":"memcached_commands_total","command":"cas","instance":"127.0.0.1:9150","job":"memcached","mysql_version":"5.7","status":"miss"},"value":[1533735286.809,"0"]},{"metric":{"__name__":"memcached_commands_total","command":"decr","instance":"127.0.0.1:9150","job":"memcached","mysql_version":"5.7","status":"hit"},"value":[1533735286.809,"0"]},{"metric":{"__name__":"memcached_commands_total","command":"decr","instance":"127.0.0.1:9150","job":"memcached","mysql_version":"5.7","status":"miss"},"value":[1533735286.809,"0"]},{"metric":{"__name__":"memcached_commands_total","command":"delete","instance":"127.0.0.1:9150","job":"memcached","mysql_version":"5.7","status":"hit"},"value":[1533735286.809,"0"]},{"metric":{"__name__":"memcached_commands_total","command":"delete","instance":"127.0.0.1:9150","job":"memcached","mysql_version":"5.7","status":"miss"},"value":[1533735286.809,"0"]},{"metric":{"__name__":"memcached_commands_total","command":"flush","instance":"127.0.0.1:9150","job":"memcached","mysql_version":"5.7","status":"hit"},"value":[1533735286.809,"0"]},{"metric":{"__name__":"memcached_commands_total","command":"get","instance":"127.0.0.1:9150","job":"memcached","mysql_version":"5.7","status":"hit"},"value":[1533735286.809,"0"]},{"metric":{"__name__":"memcached_commands_total","command":"get","instance":"127.0.0.1:9150","job":"memcached","mysql_version":"5.7","status":"miss"},"value":[1533735286.809,"0"]},{"metric":{"__name__":"memcached_commands_total","command":"incr","instance":"127.0.0.1:9150","job":"memcached","mysql_version":"5.7","status":"hit"},"value":[1533735286.809,"0"]},{"metric":{"__name__":"memcached_commands_total","command":"incr","instance":"127.0.0.1:9150","job":"memcached","mysql_version":"5.7","status":"miss"},"value":[1533735286.809,"0"]},{"metric":{"__name__":"memcached_commands_total","command":"set","instance":"127.0.0.1:9150","job":"memcached","mysql_version":"5.7","status":"hit"},"value":[1533735286.809,"0"]},{"metric":{"__name__":"memcached_commands_total","command":"touch","instance":"127.0.0.1:9150","job":"memcached","mysql_version":"5.7","status":"hit"},"value":[1533735286.809,"0"]},{"metric":{"__name__":"memcached_commands_total","command":"touch","instance":"127.0.0.1:9150","job":"memcached","mysql_version":"5.7","status":"miss"},"value":[1533735286.809,"0"]}]}}
  ```

# [Welcome pull request of other exporter](https://github.com/tomoncle/prometheus-client)

[travis]: https://travis-ci.org/tomoncle/prometheus-http-client