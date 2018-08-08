#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-8-8 下午8:06
# @Author         : Tom.Lee
# @File           : mysqld_exporter.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 
from .exporter import Exporter
from ..prometheus import prom


class MysqlExporter(Exporter):
    """
    mysql status info
    """

    @prom
    def mysql_exporter_collector_duration_seconds(self, **kwargs):
        pass

    @prom
    def mysql_exporter_last_scrape_error(self, **kwargs):
        pass

    @prom
    def mysql_exporter_scrapes_total(self, **kwargs):
        pass

    @prom
    def mysql_global_status_aborted_clients(self, **kwargs):
        pass

    @prom
    def mysql_global_status_aborted_connects(self, **kwargs):
        pass

    @prom
    def mysql_global_status_binlog_cache_disk_use(self, **kwargs):
        pass

    @prom
    def mysql_global_status_binlog_cache_use(self, **kwargs):
        pass

    @prom
    def mysql_global_status_binlog_stmt_cache_disk_use(self, **kwargs):
        pass

    @prom
    def mysql_global_status_binlog_stmt_cache_use(self, **kwargs):
        pass

    @prom
    def mysql_global_status_buffer_pool_page_changes_total(self, **kwargs):
        pass

    @prom
    def mysql_global_status_buffer_pool_pages(self, **kwargs):
        pass

    @prom
    def mysql_global_status_bytes_received(self, **kwargs):
        pass

    @prom
    def mysql_global_status_bytes_sent(self, **kwargs):
        pass

    @prom
    def mysql_global_status_commands_total(self, **kwargs):
        pass

    @prom
    def mysql_global_status_connection_errors_total(self, **kwargs):
        pass

    @prom
    def mysql_global_status_connections(self, **kwargs):
        pass

    @prom
    def mysql_global_status_created_tmp_disk_tables(self, **kwargs):
        pass

    @prom
    def mysql_global_status_created_tmp_files(self, **kwargs):
        pass

    @prom
    def mysql_global_status_created_tmp_tables(self, **kwargs):
        pass

    @prom
    def mysql_global_status_delayed_errors(self, **kwargs):
        pass

    @prom
    def mysql_global_status_delayed_insert_threads(self, **kwargs):
        pass

    @prom
    def mysql_global_status_delayed_writes(self, **kwargs):
        pass

    @prom
    def mysql_global_status_flush_commands(self, **kwargs):
        pass

    @prom
    def mysql_global_status_handlers_total(self, **kwargs):
        pass

    @prom
    def mysql_global_status_innodb_available_undo_logs(self, **kwargs):
        pass

    @prom
    def mysql_global_status_innodb_buffer_pool_bytes_data(self, **kwargs):
        pass

    @prom
    def mysql_global_status_innodb_buffer_pool_bytes_dirty(self, **kwargs):
        pass

    @prom
    def mysql_global_status_innodb_buffer_pool_read_ahead(self, **kwargs):
        pass

    @prom
    def mysql_global_status_innodb_buffer_pool_read_ahead_evicted(self, **kwargs):
        pass

    @prom
    def mysql_global_status_innodb_buffer_pool_read_ahead_rnd(self, **kwargs):
        pass

    @prom
    def mysql_global_status_innodb_buffer_pool_read_requests(self, **kwargs):
        pass

    @prom
    def mysql_global_status_innodb_buffer_pool_reads(self, **kwargs):
        pass

    @prom
    def mysql_global_status_innodb_buffer_pool_wait_free(self, **kwargs):
        pass

    @prom
    def mysql_global_status_innodb_buffer_pool_write_requests(self, **kwargs):
        pass

    @prom
    def mysql_global_status_innodb_data_fsyncs(self, **kwargs):
        pass

    @prom
    def mysql_global_status_innodb_data_pending_fsyncs(self, **kwargs):
        pass

    @prom
    def mysql_global_status_innodb_data_pending_reads(self, **kwargs):
        pass

    @prom
    def mysql_global_status_innodb_data_pending_writes(self, **kwargs):
        pass

    @prom
    def mysql_global_status_innodb_data_read(self, **kwargs):
        pass

    @prom
    def mysql_global_status_innodb_data_reads(self, **kwargs):
        pass

    @prom
    def mysql_global_status_innodb_data_writes(self, **kwargs):
        pass

    @prom
    def mysql_global_status_innodb_data_written(self, **kwargs):
        pass

    @prom
    def mysql_global_status_innodb_dblwr_pages_written(self, **kwargs):
        pass

    @prom
    def mysql_global_status_innodb_dblwr_writes(self, **kwargs):
        pass

    @prom
    def mysql_global_status_innodb_log_waits(self, **kwargs):
        pass

    @prom
    def mysql_global_status_innodb_log_write_requests(self, **kwargs):
        pass

    @prom
    def mysql_global_status_innodb_log_writes(self, **kwargs):
        pass

    @prom
    def mysql_global_status_innodb_num_open_files(self, **kwargs):
        pass

    @prom
    def mysql_global_status_innodb_os_log_fsyncs(self, **kwargs):
        pass

    @prom
    def mysql_global_status_innodb_os_log_pending_fsyncs(self, **kwargs):
        pass

    @prom
    def mysql_global_status_innodb_os_log_pending_writes(self, **kwargs):
        pass

    @prom
    def mysql_global_status_innodb_os_log_written(self, **kwargs):
        pass

    @prom
    def mysql_global_status_innodb_page_size(self, **kwargs):
        pass

    @prom
    def mysql_global_status_innodb_pages_created(self, **kwargs):
        pass

    @prom
    def mysql_global_status_innodb_pages_read(self, **kwargs):
        pass

    @prom
    def mysql_global_status_innodb_pages_written(self, **kwargs):
        pass

    @prom
    def mysql_global_status_innodb_row_lock_current_waits(self, **kwargs):
        pass

    @prom
    def mysql_global_status_innodb_row_lock_time(self, **kwargs):
        pass

    @prom
    def mysql_global_status_innodb_row_lock_time_avg(self, **kwargs):
        pass

    @prom
    def mysql_global_status_innodb_row_lock_time_max(self, **kwargs):
        pass

    @prom
    def mysql_global_status_innodb_row_lock_waits(self, **kwargs):
        pass

    @prom
    def mysql_global_status_innodb_row_ops_total(self, **kwargs):
        pass

    @prom
    def mysql_global_status_innodb_truncated_status_writes(self, **kwargs):
        pass

    @prom
    def mysql_global_status_key_blocks_not_flushed(self, **kwargs):
        pass

    @prom
    def mysql_global_status_key_blocks_unused(self, **kwargs):
        pass

    @prom
    def mysql_global_status_key_blocks_used(self, **kwargs):
        pass

    @prom
    def mysql_global_status_key_read_requests(self, **kwargs):
        pass

    @prom
    def mysql_global_status_key_reads(self, **kwargs):
        pass

    @prom
    def mysql_global_status_key_write_requests(self, **kwargs):
        pass

    @prom
    def mysql_global_status_key_writes(self, **kwargs):
        pass

    @prom
    def mysql_global_status_locked_connects(self, **kwargs):
        pass

    @prom
    def mysql_global_status_max_execution_time_exceeded(self, **kwargs):
        pass

    @prom
    def mysql_global_status_max_execution_time_set(self, **kwargs):
        pass

    @prom
    def mysql_global_status_max_execution_time_set_failed(self, **kwargs):
        pass

    @prom
    def mysql_global_status_max_used_connections(self, **kwargs):
        pass

    @prom
    def mysql_global_status_not_flushed_delayed_rows(self, **kwargs):
        pass

    @prom
    def mysql_global_status_ongoing_anonymous_transaction_count(self, **kwargs):
        pass

    @prom
    def mysql_global_status_open_files(self, **kwargs):
        pass

    @prom
    def mysql_global_status_open_streams(self, **kwargs):
        pass

    @prom
    def mysql_global_status_open_table_definitions(self, **kwargs):
        pass

    @prom
    def mysql_global_status_open_tables(self, **kwargs):
        pass

    @prom
    def mysql_global_status_opened_files(self, **kwargs):
        pass

    @prom
    def mysql_global_status_opened_table_definitions(self, **kwargs):
        pass

    @prom
    def mysql_global_status_opened_tables(self, **kwargs):
        pass

    @prom
    def mysql_global_status_performance_schema_lost_total(self, **kwargs):
        pass

    @prom
    def mysql_global_status_prepared_stmt_count(self, **kwargs):
        pass

    @prom
    def mysql_global_status_qcache_free_blocks(self, **kwargs):
        pass

    @prom
    def mysql_global_status_qcache_free_memory(self, **kwargs):
        pass

    @prom
    def mysql_global_status_qcache_hits(self, **kwargs):
        pass

    @prom
    def mysql_global_status_qcache_inserts(self, **kwargs):
        pass

    @prom
    def mysql_global_status_qcache_lowmem_prunes(self, **kwargs):
        pass

    @prom
    def mysql_global_status_qcache_not_cached(self, **kwargs):
        pass

    @prom
    def mysql_global_status_qcache_queries_in_cache(self, **kwargs):
        pass

    @prom
    def mysql_global_status_qcache_total_blocks(self, **kwargs):
        pass

    @prom
    def mysql_global_status_queries(self, **kwargs):
        pass

    @prom
    def mysql_global_status_questions(self, **kwargs):
        pass

    @prom
    def mysql_global_status_select_full_join(self, **kwargs):
        pass

    @prom
    def mysql_global_status_select_full_range_join(self, **kwargs):
        pass

    @prom
    def mysql_global_status_select_range(self, **kwargs):
        pass

    @prom
    def mysql_global_status_select_range_check(self, **kwargs):
        pass

    @prom
    def mysql_global_status_select_scan(self, **kwargs):
        pass

    @prom
    def mysql_global_status_slave_open_temp_tables(self, **kwargs):
        pass

    @prom
    def mysql_global_status_slow_launch_threads(self, **kwargs):
        pass

    @prom
    def mysql_global_status_slow_queries(self, **kwargs):
        pass

    @prom
    def mysql_global_status_sort_merge_passes(self, **kwargs):
        pass

    @prom
    def mysql_global_status_sort_range(self, **kwargs):
        pass

    @prom
    def mysql_global_status_sort_rows(self, **kwargs):
        pass

    @prom
    def mysql_global_status_sort_scan(self, **kwargs):
        pass

    @prom
    def mysql_global_status_ssl_accept_renegotiates(self, **kwargs):
        pass

    @prom
    def mysql_global_status_ssl_accepts(self, **kwargs):
        pass

    @prom
    def mysql_global_status_ssl_callback_cache_hits(self, **kwargs):
        pass

    @prom
    def mysql_global_status_ssl_client_connects(self, **kwargs):
        pass

    @prom
    def mysql_global_status_ssl_connect_renegotiates(self, **kwargs):
        pass

    @prom
    def mysql_global_status_ssl_ctx_verify_depth(self, **kwargs):
        pass

    @prom
    def mysql_global_status_ssl_ctx_verify_mode(self, **kwargs):
        pass

    @prom
    def mysql_global_status_ssl_default_timeout(self, **kwargs):
        pass

    @prom
    def mysql_global_status_ssl_finished_accepts(self, **kwargs):
        pass

    @prom
    def mysql_global_status_ssl_finished_connects(self, **kwargs):
        pass

    @prom
    def mysql_global_status_ssl_session_cache_hits(self, **kwargs):
        pass

    @prom
    def mysql_global_status_ssl_session_cache_misses(self, **kwargs):
        pass

    @prom
    def mysql_global_status_ssl_session_cache_overflows(self, **kwargs):
        pass

    @prom
    def mysql_global_status_ssl_session_cache_size(self, **kwargs):
        pass

    @prom
    def mysql_global_status_ssl_session_cache_timeouts(self, **kwargs):
        pass

    @prom
    def mysql_global_status_ssl_sessions_reused(self, **kwargs):
        pass

    @prom
    def mysql_global_status_ssl_used_session_cache_entries(self, **kwargs):
        pass

    @prom
    def mysql_global_status_ssl_verify_depth(self, **kwargs):
        pass

    @prom
    def mysql_global_status_ssl_verify_mode(self, **kwargs):
        pass

    @prom
    def mysql_global_status_table_locks_immediate(self, **kwargs):
        pass

    @prom
    def mysql_global_status_table_locks_waited(self, **kwargs):
        pass

    @prom
    def mysql_global_status_table_open_cache_hits(self, **kwargs):
        pass

    @prom
    def mysql_global_status_table_open_cache_misses(self, **kwargs):
        pass

    @prom
    def mysql_global_status_table_open_cache_overflows(self, **kwargs):
        pass

    @prom
    def mysql_global_status_tc_log_max_pages_used(self, **kwargs):
        pass

    @prom
    def mysql_global_status_tc_log_page_size(self, **kwargs):
        pass

    @prom
    def mysql_global_status_tc_log_page_waits(self, **kwargs):
        pass

    @prom
    def mysql_global_status_threads_cached(self, **kwargs):
        pass

    @prom
    def mysql_global_status_threads_connected(self, **kwargs):
        pass

    @prom
    def mysql_global_status_threads_created(self, **kwargs):
        pass

    @prom
    def mysql_global_status_threads_running(self, **kwargs):
        pass

    @prom
    def mysql_global_status_uptime(self, **kwargs):
        pass

    @prom
    def mysql_global_status_uptime_since_flush_status(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_auto_increment_increment(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_auto_increment_offset(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_autocommit(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_automatic_sp_privileges(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_avoid_temporal_upgrade(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_back_log(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_big_tables(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_binlog_cache_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_binlog_direct_non_transactional_updates(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_binlog_group_commit_sync_delay(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_binlog_group_commit_sync_no_delay_count(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_binlog_gtid_simple_recovery(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_binlog_max_flush_queue_time(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_binlog_order_commits(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_binlog_rows_query_log_events(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_binlog_stmt_cache_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_bulk_insert_buffer_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_check_proxy_users(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_connect_timeout(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_core_file(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_default_password_lifetime(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_default_week_format(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_delay_key_write(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_delayed_insert_limit(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_delayed_insert_timeout(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_delayed_queue_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_disconnect_on_expired_password(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_div_precision_increment(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_end_markers_in_json(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_enforce_gtid_consistency(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_eq_range_index_dive_limit(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_event_scheduler(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_expire_logs_days(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_explicit_defaults_for_timestamp(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_flush(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_flush_time(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_foreign_key_checks(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_ft_max_word_len(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_ft_min_word_len(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_ft_query_expansion_limit(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_general_log(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_group_concat_max_len(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_gtid_executed_compression_period(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_gtid_mode(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_host_cache_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_ignore_builtin_innodb(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_adaptive_flushing(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_adaptive_flushing_lwm(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_adaptive_hash_index(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_adaptive_hash_index_parts(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_adaptive_max_sleep_delay(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_api_bk_commit_interval(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_api_disable_rowlock(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_api_enable_binlog(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_api_enable_mdl(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_api_trx_level(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_autoextend_increment(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_autoinc_lock_mode(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_buffer_pool_chunk_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_buffer_pool_dump_at_shutdown(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_buffer_pool_dump_now(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_buffer_pool_dump_pct(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_buffer_pool_instances(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_buffer_pool_load_abort(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_buffer_pool_load_at_startup(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_buffer_pool_load_now(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_buffer_pool_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_change_buffer_max_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_checksums(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_cmp_per_index_enabled(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_commit_concurrency(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_compression_failure_threshold_pct(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_compression_level(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_compression_pad_pct_max(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_concurrency_tickets(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_deadlock_detect(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_disable_sort_file_cache(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_doublewrite(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_fast_shutdown(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_file_format_check(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_file_per_table(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_fill_factor(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_flush_log_at_timeout(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_flush_log_at_trx_commit(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_flush_neighbors(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_flush_sync(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_flushing_avg_loops(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_force_load_corrupted(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_force_recovery(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_ft_cache_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_ft_enable_diag_print(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_ft_enable_stopword(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_ft_max_token_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_ft_min_token_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_ft_num_word_optimize(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_ft_result_cache_limit(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_ft_sort_pll_degree(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_ft_total_cache_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_io_capacity(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_io_capacity_max(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_large_prefix(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_lock_wait_timeout(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_locks_unsafe_for_binlog(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_log_buffer_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_log_checksums(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_log_compressed_pages(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_log_file_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_log_files_in_group(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_log_write_ahead_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_lru_scan_depth(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_max_dirty_pages_pct(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_max_dirty_pages_pct_lwm(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_max_purge_lag(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_max_purge_lag_delay(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_max_undo_log_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_old_blocks_pct(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_old_blocks_time(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_online_alter_log_max_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_open_files(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_optimize_fulltext_only(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_page_cleaners(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_page_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_print_all_deadlocks(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_purge_batch_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_purge_rseg_truncate_frequency(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_purge_threads(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_random_read_ahead(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_read_ahead_threshold(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_read_io_threads(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_read_only(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_replication_delay(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_rollback_on_timeout(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_rollback_segments(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_sort_buffer_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_spin_wait_delay(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_stats_auto_recalc(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_stats_on_metadata(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_stats_persistent(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_stats_persistent_sample_pages(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_stats_sample_pages(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_stats_transient_sample_pages(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_status_output(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_status_output_locks(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_strict_mode(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_support_xa(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_sync_array_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_sync_spin_loops(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_table_locks(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_thread_concurrency(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_thread_sleep_delay(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_undo_log_truncate(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_undo_logs(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_undo_tablespaces(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_use_native_aio(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_innodb_write_io_threads(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_interactive_timeout(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_join_buffer_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_keep_files_on_create(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_key_buffer_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_key_cache_age_threshold(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_key_cache_block_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_key_cache_division_limit(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_large_files_support(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_large_page_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_large_pages(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_local_infile(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_lock_wait_timeout(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_locked_in_memory(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_log_bin(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_log_bin_trust_function_creators(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_log_bin_use_v1_row_events(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_log_builtin_as_identified_by_password(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_log_error_verbosity(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_log_queries_not_using_indexes(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_log_slave_updates(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_log_slow_admin_statements(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_log_slow_slave_statements(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_log_statements_unsafe_for_binlog(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_log_syslog(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_log_syslog_include_pid(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_log_throttle_queries_not_using_indexes(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_log_warnings(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_long_query_time(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_low_priority_updates(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_lower_case_file_system(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_lower_case_table_names(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_master_verify_checksum(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_max_allowed_packet(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_max_binlog_cache_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_max_binlog_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_max_binlog_stmt_cache_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_max_connect_errors(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_max_connections(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_max_delayed_threads(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_max_digest_length(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_max_error_count(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_max_execution_time(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_max_heap_table_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_max_insert_delayed_threads(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_max_join_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_max_length_for_sort_data(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_max_points_in_geometry(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_max_prepared_stmt_count(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_max_relay_log_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_max_seeks_for_key(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_max_sort_length(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_max_sp_recursion_depth(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_max_tmp_tables(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_max_user_connections(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_max_write_lock_count(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_metadata_locks_cache_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_metadata_locks_hash_instances(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_min_examined_row_limit(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_multi_range_count(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_myisam_data_pointer_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_myisam_max_sort_file_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_myisam_mmap_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_myisam_recover_options(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_myisam_repair_threads(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_myisam_sort_buffer_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_myisam_use_mmap(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_mysql_native_password_proxy_users(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_net_buffer_length(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_net_read_timeout(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_net_retry_count(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_net_write_timeout(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_new(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_ngram_token_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_offline_mode(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_old(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_old_alter_table(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_old_passwords(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_open_files_limit(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_optimizer_prune_level(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_optimizer_search_depth(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_optimizer_trace_limit(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_optimizer_trace_max_mem_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_optimizer_trace_offset(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_parser_max_mem_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema_accounts_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema_digests_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema_events_stages_history_long_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema_events_stages_history_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema_events_statements_history_long_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema_events_statements_history_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema_events_transactions_history_long_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema_events_transactions_history_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema_events_waits_history_long_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema_events_waits_history_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema_hosts_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema_max_cond_classes(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema_max_cond_instances(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema_max_digest_length(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema_max_file_classes(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema_max_file_handles(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema_max_file_instances(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema_max_index_stat(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema_max_memory_classes(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema_max_metadata_locks(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema_max_mutex_classes(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema_max_mutex_instances(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema_max_prepared_statements_instances(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema_max_program_instances(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema_max_rwlock_classes(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema_max_rwlock_instances(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema_max_socket_classes(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema_max_socket_instances(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema_max_sql_text_length(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema_max_stage_classes(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema_max_statement_classes(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema_max_statement_stack(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema_max_table_handles(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema_max_table_instances(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema_max_table_lock_stat(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema_max_thread_classes(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema_max_thread_instances(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema_session_connect_attrs_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema_setup_actors_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema_setup_objects_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_performance_schema_users_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_port(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_preload_buffer_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_profiling(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_profiling_history_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_protocol_version(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_query_alloc_block_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_query_cache_limit(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_query_cache_min_res_unit(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_query_cache_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_query_cache_type(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_query_cache_wlock_invalidate(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_query_prealloc_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_range_alloc_block_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_range_optimizer_max_mem_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_read_buffer_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_read_only(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_read_rnd_buffer_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_relay_log_purge(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_relay_log_recovery(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_relay_log_space_limit(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_report_port(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_require_secure_transport(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_rpl_stop_slave_timeout(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_secure_auth(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_server_id(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_server_id_bits(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_session_track_gtids(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_session_track_schema(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_session_track_state_change(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_session_track_transaction_info(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_sha256_password_proxy_users(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_show_compatibility_56(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_show_old_temporals(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_skip_external_locking(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_skip_name_resolve(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_skip_networking(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_skip_show_database(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_slave_allow_batching(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_slave_checkpoint_group(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_slave_checkpoint_period(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_slave_compressed_protocol(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_slave_max_allowed_packet(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_slave_net_timeout(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_slave_parallel_workers(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_slave_pending_jobs_size_max(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_slave_preserve_commit_order(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_slave_skip_errors(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_slave_sql_verify_checksum(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_slave_transaction_retries(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_slow_launch_time(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_slow_query_log(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_sort_buffer_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_sql_auto_is_null(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_sql_big_selects(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_sql_buffer_result(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_sql_log_off(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_sql_notes(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_sql_quote_show_create(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_sql_safe_updates(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_sql_select_limit(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_sql_slave_skip_counter(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_sql_warnings(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_stored_program_cache(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_super_read_only(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_sync_binlog(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_sync_frm(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_sync_master_info(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_sync_relay_log(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_sync_relay_log_info(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_table_definition_cache(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_table_open_cache(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_table_open_cache_instances(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_thread_cache_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_thread_stack(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_tmp_table_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_transaction_alloc_block_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_transaction_prealloc_size(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_transaction_write_set_extraction(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_tx_read_only(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_unique_checks(self, **kwargs):
        pass

    @prom
    def mysql_global_variables_wait_timeout(self, **kwargs):
        pass

    @prom
    def mysql_info_schema_table_rows(self, **kwargs):
        pass

    @prom
    def mysql_info_schema_table_size(self, **kwargs):
        pass

    @prom
    def mysql_info_schema_table_version(self, **kwargs):
        pass

    @prom
    def mysql_up(self, **kwargs):
        pass

    @prom
    def mysql_version_info(self, **kwargs):
        pass

    @prom
    def mysqld_exporter_build_info(self, **kwargs):
        pass
