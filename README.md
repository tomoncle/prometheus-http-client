# Prometheus-http-client [![Build Status](https://travis-ci.org/tomoncle/prometheus-http-client.svg?branch=master)][travis]
> Prometheus service http client, convenient query client，asy to expand custom functions．

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
  * Paramters:
    * `graph`: True/False                                        , default False
    * `start`: timestamp                                         , if graph is True, necessary
    * `end`  : timestamp                                         , if graph is True, necessary
    * `step` : int (graph point step size)                       , default None
    * `time` : timestamp                                         , default time.time()
    * `filter`: {'instance':'127.0.0.1', 'label':'go lang', ...}  , default None
  * return json data.
  * examples :
    ```python
    Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
    [GCC 4.8.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 
    >>> from prometheus_http_client import NodeExporter
    >>> node_exporter = NodeExporter()
    >>> node_exporter.node_cpu_rate(filter={'instance': '127.0.0.1:9100','mode':'user','job':'static_nodes'})
    u'{"status":"success","data":{"resultType":"vector","result":[{"metric":{"instance":"127.0.0.1:9100","job":"static_nodes"},"value":[1533779495.799,"70.7333333333338"]}]}}'
    >>> 
    >>> node_exporter.node_cpu_rate(filter={'instance': '127.0.0.1:9100','job':'static_nodes'})
    u'{"status":"success","data":{"resultType":"vector","result":[{"metric":{"instance":"127.0.0.1:9100","job":"static_nodes"},"value":[1533779522.109,"2.2500000000051443"]}]}}'
    >>> 
    ```


## Install
* source:
```shell
$ git clone https://github.com/tomoncle/prometheus-http-client.git
$ cd prometheus-http-client && sudo python setup.py install
```

* pip: `$ pip install prometheus-http-client`

## Config
* default config : `http://localhost:9090`
* change config  : `$ export PROMETHEUS_URL='http://192.168.1.2:9090'`
* auth config    : `$ export PROMETHEUS_HEAD='{"Cookie": "123456"}'`

## Query
### Prometheus
  ```python
   Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
  [GCC 4.8.2] on linux2
  Type "help", "copyright", "credits" or "license" for more information.
  >>> 
  >>> from prometheus_http_client import Prometheus
  >>> prometheus = Prometheus()
  >>> prometheus.query(metric='irate(node_cpu{job="static_nodes"}[5m])')
  u'{"status":"success","data":{"resultType":"vector","result":[{"metric":{"cpu":"cpu0","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"idle"},"value":[1533779660.16,"0.9340000000001358"]},{"metric":{"cpu":"cpu0","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"iowait"},"value":[1533779660.16,"0.003333333333334091"]},{"metric":{"cpu":"cpu0","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"irq"},"value":[1533779660.16,"0"]},{"metric":{"cpu":"cpu0","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"nice"},"value":[1533779660.16,"0"]},{"metric":{"cpu":"cpu0","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"softirq"},"value":[1533779660.16,"0"]},{"metric":{"cpu":"cpu0","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"steal"},"value":[1533779660.16,"0"]},{"metric":{"cpu":"cpu0","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"system"},"value":[1533779660.16,"0.016666666666666666"]},{"metric":{"cpu":"cpu0","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"user"},"value":[1533779660.16,"0.025333333333340608"]},{"metric":{"cpu":"cpu1","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"idle"},"value":[1533779660.16,"0.9373333333333297"]},{"metric":{"cpu":"cpu1","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"iowait"},"value":[1533779660.16,"0.025333333333333503"]},{"metric":{"cpu":"cpu1","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"irq"},"value":[1533779660.16,"0"]},{"metric":{"cpu":"cpu1","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"nice"},"value":[1533779660.16,"0"]},{"metric":{"cpu":"cpu1","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"softirq"},"value":[1533779660.16,"0"]},{"metric":{"cpu":"cpu1","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"steal"},"value":[1533779660.16,"0"]},{"metric":{"cpu":"cpu1","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"system"},"value":[1533779660.16,"0.0073333333333304536"]},{"metric":{"cpu":"cpu1","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"user"},"value":[1533779660.16,"0.02333333333332727"]},{"metric":{"cpu":"cpu2","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"idle"},"value":[1533779660.16,"0.9486666666666679"]},{"metric":{"cpu":"cpu2","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"iowait"},"value":[1533779660.16,"0"]},{"metric":{"cpu":"cpu2","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"irq"},"value":[1533779660.16,"0"]},{"metric":{"cpu":"cpu2","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"nice"},"value":[1533779660.16,"0"]},{"metric":{"cpu":"cpu2","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"softirq"},"value":[1533779660.16,"0"]},{"metric":{"cpu":"cpu2","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"steal"},"value":[1533779660.16,"0"]},{"metric":{"cpu":"cpu2","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"system"},"value":[1533779660.16,"0.009333333333332423"]},{"metric":{"cpu":"cpu2","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"user"},"value":[1533779660.16,"0.0319999999999709"]},{"metric":{"cpu":"cpu3","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"idle"},"value":[1533779660.16,"0.9540000000000267"]},{"metric":{"cpu":"cpu3","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"iowait"},"value":[1533779660.16,"0.0006666666666670077"]},{"metric":{"cpu":"cpu3","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"irq"},"value":[1533779660.16,"0"]},{"metric":{"cpu":"cpu3","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"nice"},"value":[1533779660.16,"0"]},{"metric":{"cpu":"cpu3","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"softirq"},"value":[1533779660.16,"0"]},{"metric":{"cpu":"cpu3","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"steal"},"value":[1533779660.16,"0"]},{"metric":{"cpu":"cpu3","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"system"},"value":[1533779660.16,"0.008666666666666363"]},{"metric":{"cpu":"cpu3","device_ID":"static_node","instance":"127.0.0.1:9100","job":"static_nodes","mode":"user"},"value":[1533779660.16,"0.03266666666665211"]}]}}'
  >>> 
  >>> prometheus.query(metric='sum by (mode, instance,job) (irate(node_cpu{job="static_nodes"}[5m]))')
u'{"status":"success","data":{"resultType":"vector","result":[{"metric":{"instance":"127.0.0.1:9100","job":"static_nodes","mode":"system"},"value":[1533779830.339,"0.038000000000010914"]},{"metric":{"instance":"127.0.0.1:9100","job":"static_nodes","mode":"user"},"value":[1533779830.339,"0.09133333333332606"]},{"metric":{"instance":"127.0.0.1:9100","job":"static_nodes","mode":"idle"},"value":[1533779830.339,"3.8"]},{"metric":{"instance":"127.0.0.1:9100","job":"static_nodes","mode":"iowait"},"value":[1533779830.339,"0.035333333333332696"]},{"metric":{"instance":"127.0.0.1:9100","job":"static_nodes","mode":"irq"},"value":[1533779830.339,"0"]},{"metric":{"instance":"127.0.0.1:9100","job":"static_nodes","mode":"nice"},"value":[1533779830.339,"0"]},{"metric":{"instance":"127.0.0.1:9100","job":"static_nodes","mode":"softirq"},"value":[1533779830.339,"0.0006666666666666524"]},{"metric":{"instance":"127.0.0.1:9100","job":"static_nodes","mode":"steal"},"value":[1533779830.339,"0"]}]}}'
  >>> 
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


### [Welcome pull request of other exporter](https://github.com/tomoncle/prometheus-http-client)

[travis]: https://travis-ci.org/tomoncle/prometheus-http-client
