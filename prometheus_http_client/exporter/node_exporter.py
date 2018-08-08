#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-8-7 下午4:02
# @Author         : Tom.Lee
# @File           : node_exporter.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 
from .exporter import Exporter
from ..prometheus import prom
from ..prometheus import relabel


class NodeExporter(Exporter):
    """
    linux system status
    """

    @prom
    def node_arp_entries(self, **kwargs):
        pass

    @prom
    def node_boot_time(self, **kwargs):
        pass

    @prom
    def node_context_switches(self, **kwargs):
        pass

    @prom
    def node_cpu(self, **kwargs):
        pass

    @prom
    def node_cpu_core_throttles_total(self, **kwargs):
        pass

    @prom
    def node_cpu_frequency_hertz(self, **kwargs):
        pass

    @prom
    def node_cpu_frequency_max_hertz(self, **kwargs):
        pass

    @prom
    def node_cpu_frequency_min_hertz(self, **kwargs):
        pass

    @prom
    def node_cpu_guest_seconds_total(self, **kwargs):
        pass

    @prom
    def node_cpu_package_throttles_total(self, **kwargs):
        pass

    @prom
    def node_disk_bytes_read(self, **kwargs):
        pass

    @prom
    def node_disk_bytes_written(self, **kwargs):
        pass

    @prom
    def node_disk_io_now(self, **kwargs):
        pass

    @prom
    def node_disk_io_time_ms(self, **kwargs):
        pass

    @prom
    def node_disk_io_time_weighted(self, **kwargs):
        pass

    @prom
    def node_disk_read_time_ms(self, **kwargs):
        pass

    @prom
    def node_disk_reads_completed(self, **kwargs):
        pass

    @prom
    def node_disk_reads_merged(self, **kwargs):
        pass

    @prom
    def node_disk_sectors_read(self, **kwargs):
        pass

    @prom
    def node_disk_sectors_written(self, **kwargs):
        pass

    @prom
    def node_disk_write_time_ms(self, **kwargs):
        pass

    @prom
    def node_disk_writes_completed(self, **kwargs):
        pass

    @prom
    def node_disk_writes_merged(self, **kwargs):
        pass

    @prom
    def node_entropy_available_bits(self, **kwargs):
        pass

    @prom
    def node_exporter_build_info(self, **kwargs):
        pass

    @prom
    def node_filefd_allocated(self, **kwargs):
        pass

    @prom
    def node_filefd_maximum(self, **kwargs):
        pass

    @prom
    def node_filesystem_avail(self, **kwargs):
        pass

    @prom
    def node_filesystem_device_error(self, **kwargs):
        pass

    @prom
    def node_filesystem_files(self, **kwargs):
        pass

    @prom
    def node_filesystem_files_free(self, **kwargs):
        pass

    @prom
    def node_filesystem_free(self, **kwargs):
        pass

    @prom
    def node_filesystem_readonly(self, **kwargs):
        pass

    @prom
    def node_filesystem_size(self, **kwargs):
        pass

    @prom
    def node_forks(self, **kwargs):
        pass

    @prom
    def node_hwmon_chip_names(self, **kwargs):
        pass

    @prom
    def node_hwmon_fan_rpm(self, **kwargs):
        pass

    @prom
    def node_hwmon_pwm(self, **kwargs):
        pass

    @prom
    def node_hwmon_pwm_enable(self, **kwargs):
        pass

    @prom
    def node_hwmon_sensor_label(self, **kwargs):
        pass

    @prom
    def node_hwmon_temp_celsius(self, **kwargs):
        pass

    @prom
    def node_hwmon_temp_crit_alarm_celsius(self, **kwargs):
        pass

    @prom
    def node_hwmon_temp_crit_celsius(self, **kwargs):
        pass

    @prom
    def node_hwmon_temp_crit_hyst_celsius(self, **kwargs):
        pass

    @prom
    def node_hwmon_temp_max_celsius(self, **kwargs):
        pass

    @prom
    def node_intr(self, **kwargs):
        pass

    @prom
    def node_load1(self, **kwargs):
        pass

    @prom
    def node_load15(self, **kwargs):
        pass

    @prom
    def node_load5(self, **kwargs):
        pass

    @prom
    def node_memory_Active(self, **kwargs):
        pass

    @prom
    def node_memory_Active_anon(self, **kwargs):
        pass

    @prom
    def node_memory_Active_file(self, **kwargs):
        pass

    @prom
    def node_memory_AnonHugePages(self, **kwargs):
        pass

    @prom
    def node_memory_AnonPages(self, **kwargs):
        pass

    @prom
    def node_memory_Bounce(self, **kwargs):
        pass

    @prom
    def node_memory_Buffers(self, **kwargs):
        pass

    @prom
    def node_memory_Cached(self, **kwargs):
        pass

    @prom
    def node_memory_CmaFree(self, **kwargs):
        pass

    @prom
    def node_memory_CmaTotal(self, **kwargs):
        pass

    @prom
    def node_memory_CommitLimit(self, **kwargs):
        pass

    @prom
    def node_memory_Committed_AS(self, **kwargs):
        pass

    @prom
    def node_memory_DirectMap1G(self, **kwargs):
        pass

    @prom
    def node_memory_DirectMap2M(self, **kwargs):
        pass

    @prom
    def node_memory_DirectMap4k(self, **kwargs):
        pass

    @prom
    def node_memory_Dirty(self, **kwargs):
        pass

    @prom
    def node_memory_HardwareCorrupted(self, **kwargs):
        pass

    @prom
    def node_memory_HugePages_Free(self, **kwargs):
        pass

    @prom
    def node_memory_HugePages_Rsvd(self, **kwargs):
        pass

    @prom
    def node_memory_HugePages_Surp(self, **kwargs):
        pass

    @prom
    def node_memory_HugePages_Total(self, **kwargs):
        pass

    @prom
    def node_memory_Hugepagesize(self, **kwargs):
        pass

    @prom
    def node_memory_Inactive(self, **kwargs):
        pass

    @prom
    def node_memory_Inactive_anon(self, **kwargs):
        pass

    @prom
    def node_memory_Inactive_file(self, **kwargs):
        pass

    @prom
    def node_memory_KernelStack(self, **kwargs):
        pass

    @prom
    def node_memory_Mapped(self, **kwargs):
        pass

    @prom
    def node_memory_MemAvailable(self, **kwargs):
        pass

    @prom
    def node_memory_MemFree(self, **kwargs):
        pass

    @prom
    def node_memory_MemTotal(self, **kwargs):
        pass

    @prom
    def node_memory_Mlocked(self, **kwargs):
        pass

    @prom
    def node_memory_NFS_Unstable(self, **kwargs):
        pass

    @prom
    def node_memory_PageTables(self, **kwargs):
        pass

    @prom
    def node_memory_SReclaimable(self, **kwargs):
        pass

    @prom
    def node_memory_SUnreclaim(self, **kwargs):
        pass

    @prom
    def node_memory_Shmem(self, **kwargs):
        pass

    @prom
    def node_memory_Slab(self, **kwargs):
        pass

    @prom
    def node_memory_SwapCached(self, **kwargs):
        pass

    @prom
    def node_memory_SwapFree(self, **kwargs):
        pass

    @prom
    def node_memory_SwapTotal(self, **kwargs):
        pass

    @prom
    def node_memory_Unevictable(self, **kwargs):
        pass

    @prom
    def node_memory_VmallocChunk(self, **kwargs):
        pass

    @prom
    def node_memory_VmallocTotal(self, **kwargs):
        pass

    @prom
    def node_memory_VmallocUsed(self, **kwargs):
        pass

    @prom
    def node_memory_Writeback(self, **kwargs):
        pass

    @prom
    def node_memory_WritebackTmp(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_InCsumErrors(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_InDestUnreachs(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_InEchoReplies(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_InEchos(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_InErrors(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_InGroupMembQueries(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_InGroupMembReductions(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_InGroupMembResponses(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_InMLDv2Reports(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_InMsgs(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_InNeighborAdvertisements(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_InNeighborSolicits(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_InParmProblems(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_InPktTooBigs(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_InRedirects(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_InRouterAdvertisements(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_InRouterSolicits(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_InTimeExcds(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_InType1(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_InType134(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_InType135(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_OutDestUnreachs(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_OutEchoReplies(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_OutEchos(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_OutErrors(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_OutGroupMembQueries(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_OutGroupMembReductions(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_OutGroupMembResponses(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_OutMLDv2Reports(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_OutMsgs(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_OutNeighborAdvertisements(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_OutNeighborSolicits(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_OutParmProblems(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_OutPktTooBigs(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_OutRedirects(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_OutRouterAdvertisements(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_OutRouterSolicits(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_OutTimeExcds(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_OutType1(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_OutType133(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_OutType135(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp6_OutType143(self, **kwargs):
        pass

    @prom
    def node_netstat_IcmpMsg_InType3(self, **kwargs):
        pass

    @prom
    def node_netstat_IcmpMsg_OutType3(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp_InAddrMaskReps(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp_InAddrMasks(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp_InCsumErrors(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp_InDestUnreachs(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp_InEchoReps(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp_InEchos(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp_InErrors(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp_InMsgs(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp_InParmProbs(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp_InRedirects(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp_InSrcQuenchs(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp_InTimeExcds(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp_InTimestampReps(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp_InTimestamps(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp_OutAddrMaskReps(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp_OutAddrMasks(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp_OutDestUnreachs(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp_OutEchoReps(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp_OutEchos(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp_OutErrors(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp_OutMsgs(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp_OutParmProbs(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp_OutRedirects(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp_OutSrcQuenchs(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp_OutTimeExcds(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp_OutTimestampReps(self, **kwargs):
        pass

    @prom
    def node_netstat_Icmp_OutTimestamps(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip6_FragCreates(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip6_FragFails(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip6_FragOKs(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip6_InAddrErrors(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip6_InBcastOctets(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip6_InCEPkts(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip6_InDelivers(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip6_InDiscards(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip6_InECT0Pkts(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip6_InECT1Pkts(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip6_InHdrErrors(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip6_InMcastOctets(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip6_InMcastPkts(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip6_InNoECTPkts(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip6_InNoRoutes(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip6_InOctets(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip6_InReceives(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip6_InTooBigErrors(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip6_InTruncatedPkts(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip6_InUnknownProtos(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip6_OutBcastOctets(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip6_OutDiscards(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip6_OutForwDatagrams(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip6_OutMcastOctets(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip6_OutMcastPkts(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip6_OutNoRoutes(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip6_OutOctets(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip6_OutRequests(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip6_ReasmFails(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip6_ReasmOKs(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip6_ReasmReqds(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip6_ReasmTimeout(self, **kwargs):
        pass

    @prom
    def node_netstat_IpExt_InBcastOctets(self, **kwargs):
        pass

    @prom
    def node_netstat_IpExt_InBcastPkts(self, **kwargs):
        pass

    @prom
    def node_netstat_IpExt_InCEPkts(self, **kwargs):
        pass

    @prom
    def node_netstat_IpExt_InCsumErrors(self, **kwargs):
        pass

    @prom
    def node_netstat_IpExt_InECT0Pkts(self, **kwargs):
        pass

    @prom
    def node_netstat_IpExt_InECT1Pkts(self, **kwargs):
        pass

    @prom
    def node_netstat_IpExt_InMcastOctets(self, **kwargs):
        pass

    @prom
    def node_netstat_IpExt_InMcastPkts(self, **kwargs):
        pass

    @prom
    def node_netstat_IpExt_InNoECTPkts(self, **kwargs):
        pass

    @prom
    def node_netstat_IpExt_InNoRoutes(self, **kwargs):
        pass

    @prom
    def node_netstat_IpExt_InOctets(self, **kwargs):
        pass

    @prom
    def node_netstat_IpExt_InTruncatedPkts(self, **kwargs):
        pass

    @prom
    def node_netstat_IpExt_OutBcastOctets(self, **kwargs):
        pass

    @prom
    def node_netstat_IpExt_OutBcastPkts(self, **kwargs):
        pass

    @prom
    def node_netstat_IpExt_OutMcastOctets(self, **kwargs):
        pass

    @prom
    def node_netstat_IpExt_OutMcastPkts(self, **kwargs):
        pass

    @prom
    def node_netstat_IpExt_OutOctets(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip_DefaultTTL(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip_ForwDatagrams(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip_Forwarding(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip_FragCreates(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip_FragFails(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip_FragOKs(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip_InAddrErrors(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip_InDelivers(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip_InDiscards(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip_InHdrErrors(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip_InReceives(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip_InUnknownProtos(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip_OutDiscards(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip_OutNoRoutes(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip_OutRequests(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip_ReasmFails(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip_ReasmOKs(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip_ReasmReqds(self, **kwargs):
        pass

    @prom
    def node_netstat_Ip_ReasmTimeout(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_ArpFilter(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_BusyPollRxPackets(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_DelayedACKLocked(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_DelayedACKLost(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_DelayedACKs(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_EmbryonicRsts(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_IPReversePathFilter(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_ListenDrops(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_ListenOverflows(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_LockDroppedIcmps(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_OfoPruned(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_OutOfWindowIcmps(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_PAWSActive(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_PAWSEstab(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_PAWSPassive(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_PruneCalled(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_RcvPruned(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_SyncookiesFailed(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_SyncookiesRecv(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_SyncookiesSent(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPAbortFailed(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPAbortOnClose(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPAbortOnData(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPAbortOnLinger(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPAbortOnMemory(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPAbortOnTimeout(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPAutoCorking(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPBacklogDrop(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPChallengeACK(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPDSACKIgnoredNoUndo(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPDSACKIgnoredOld(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPDSACKOfoRecv(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPDSACKOfoSent(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPDSACKOldSent(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPDSACKRecv(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPDSACKUndo(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPDeferAcceptDrop(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPDirectCopyFromBacklog(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPDirectCopyFromPrequeue(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPFACKReorder(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPFastOpenActive(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPFastOpenActiveFail(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPFastOpenCookieReqd(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPFastOpenListenOverflow(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPFastOpenPassive(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPFastOpenPassiveFail(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPFastRetrans(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPForwardRetrans(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPFromZeroWindowAdv(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPFullUndo(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPHPAcks(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPHPHits(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPHPHitsToUser(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPHystartDelayCwnd(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPHystartDelayDetect(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPHystartTrainCwnd(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPHystartTrainDetect(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPLossFailures(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPLossProbeRecovery(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPLossProbes(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPLossUndo(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPLostRetransmit(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPMD5NotFound(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPMD5Unexpected(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPMemoryPressures(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPMinTTLDrop(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPOFODrop(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPOFOMerge(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPOFOQueue(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPOrigDataSent(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPPartialUndo(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPPrequeueDropped(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPPrequeued(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPPureAcks(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPRcvCoalesce(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPRcvCollapsed(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPRenoFailures(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPRenoRecovery(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPRenoRecoveryFail(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPRenoReorder(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPReqQFullDoCookies(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPReqQFullDrop(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPRetransFail(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPSACKDiscard(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPSACKReneging(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPSACKReorder(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPSYNChallenge(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPSackFailures(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPSackMerged(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPSackRecovery(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPSackRecoveryFail(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPSackShiftFallback(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPSackShifted(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPSchedulerFailed(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPSlowStartRetrans(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPSpuriousRTOs(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPSpuriousRtxHostQueues(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPSynRetrans(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPTSReorder(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPTimeWaitOverflow(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPTimeouts(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPToZeroWindowAdv(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TCPWantZeroWindowAdv(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TW(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TWKilled(self, **kwargs):
        pass

    @prom
    def node_netstat_TcpExt_TWRecycled(self, **kwargs):
        pass

    @prom
    def node_netstat_Tcp_ActiveOpens(self, **kwargs):
        pass

    @prom
    def node_netstat_Tcp_AttemptFails(self, **kwargs):
        pass

    @prom
    def node_netstat_Tcp_CurrEstab(self, **kwargs):
        pass

    @prom
    def node_netstat_Tcp_EstabResets(self, **kwargs):
        pass

    @prom
    def node_netstat_Tcp_InCsumErrors(self, **kwargs):
        pass

    @prom
    def node_netstat_Tcp_InErrs(self, **kwargs):
        pass

    @prom
    def node_netstat_Tcp_InSegs(self, **kwargs):
        pass

    @prom
    def node_netstat_Tcp_MaxConn(self, **kwargs):
        pass

    @prom
    def node_netstat_Tcp_OutRsts(self, **kwargs):
        pass

    @prom
    def node_netstat_Tcp_OutSegs(self, **kwargs):
        pass

    @prom
    def node_netstat_Tcp_PassiveOpens(self, **kwargs):
        pass

    @prom
    def node_netstat_Tcp_RetransSegs(self, **kwargs):
        pass

    @prom
    def node_netstat_Tcp_RtoAlgorithm(self, **kwargs):
        pass

    @prom
    def node_netstat_Tcp_RtoMax(self, **kwargs):
        pass

    @prom
    def node_netstat_Tcp_RtoMin(self, **kwargs):
        pass

    @prom
    def node_netstat_Udp6_IgnoredMulti(self, **kwargs):
        pass

    @prom
    def node_netstat_Udp6_InCsumErrors(self, **kwargs):
        pass

    @prom
    def node_netstat_Udp6_InDatagrams(self, **kwargs):
        pass

    @prom
    def node_netstat_Udp6_InErrors(self, **kwargs):
        pass

    @prom
    def node_netstat_Udp6_NoPorts(self, **kwargs):
        pass

    @prom
    def node_netstat_Udp6_OutDatagrams(self, **kwargs):
        pass

    @prom
    def node_netstat_Udp6_RcvbufErrors(self, **kwargs):
        pass

    @prom
    def node_netstat_Udp6_SndbufErrors(self, **kwargs):
        pass

    @prom
    def node_netstat_UdpLite6_InCsumErrors(self, **kwargs):
        pass

    @prom
    def node_netstat_UdpLite6_InDatagrams(self, **kwargs):
        pass

    @prom
    def node_netstat_UdpLite6_InErrors(self, **kwargs):
        pass

    @prom
    def node_netstat_UdpLite6_NoPorts(self, **kwargs):
        pass

    @prom
    def node_netstat_UdpLite6_OutDatagrams(self, **kwargs):
        pass

    @prom
    def node_netstat_UdpLite6_RcvbufErrors(self, **kwargs):
        pass

    @prom
    def node_netstat_UdpLite6_SndbufErrors(self, **kwargs):
        pass

    @prom
    def node_netstat_UdpLite_IgnoredMulti(self, **kwargs):
        pass

    @prom
    def node_netstat_UdpLite_InCsumErrors(self, **kwargs):
        pass

    @prom
    def node_netstat_UdpLite_InDatagrams(self, **kwargs):
        pass

    @prom
    def node_netstat_UdpLite_InErrors(self, **kwargs):
        pass

    @prom
    def node_netstat_UdpLite_NoPorts(self, **kwargs):
        pass

    @prom
    def node_netstat_UdpLite_OutDatagrams(self, **kwargs):
        pass

    @prom
    def node_netstat_UdpLite_RcvbufErrors(self, **kwargs):
        pass

    @prom
    def node_netstat_UdpLite_SndbufErrors(self, **kwargs):
        pass

    @prom
    def node_netstat_Udp_IgnoredMulti(self, **kwargs):
        pass

    @prom
    def node_netstat_Udp_InCsumErrors(self, **kwargs):
        pass

    @prom
    def node_netstat_Udp_InDatagrams(self, **kwargs):
        pass

    @prom
    def node_netstat_Udp_InErrors(self, **kwargs):
        pass

    @prom
    def node_netstat_Udp_NoPorts(self, **kwargs):
        pass

    @prom
    def node_netstat_Udp_OutDatagrams(self, **kwargs):
        pass

    @prom
    def node_netstat_Udp_RcvbufErrors(self, **kwargs):
        pass

    @prom
    def node_netstat_Udp_SndbufErrors(self, **kwargs):
        pass

    @prom
    def node_network_receive_bytes_total(self, **kwargs):
        pass

    @prom
    def node_network_receive_compressed_total(self, **kwargs):
        pass

    @prom
    def node_network_receive_drop_total(self, **kwargs):
        pass

    @prom
    def node_network_receive_errs_total(self, **kwargs):
        pass

    @prom
    def node_network_receive_fifo_total(self, **kwargs):
        pass

    @prom
    def node_network_receive_frame_total(self, **kwargs):
        pass

    @prom
    def node_network_receive_multicast_total(self, **kwargs):
        pass

    @prom
    def node_network_receive_packets_total(self, **kwargs):
        pass

    @prom
    def node_network_transmit_bytes_total(self, **kwargs):
        pass

    @prom
    def node_network_transmit_compressed_total(self, **kwargs):
        pass

    @prom
    def node_network_transmit_drop_total(self, **kwargs):
        pass

    @prom
    def node_network_transmit_errs_total(self, **kwargs):
        pass

    @prom
    def node_network_transmit_fifo_total(self, **kwargs):
        pass

    @prom
    def node_network_transmit_frame_total(self, **kwargs):
        pass

    @prom
    def node_network_transmit_multicast_total(self, **kwargs):
        pass

    @prom
    def node_network_transmit_packets_total(self, **kwargs):
        pass

    @prom
    def node_nf_conntrack_entries(self, **kwargs):
        pass

    @prom
    def node_nf_conntrack_entries_limit(self, **kwargs):
        pass

    @prom
    def node_procs_blocked(self, **kwargs):
        pass

    @prom
    def node_procs_running(self, **kwargs):
        pass

    @prom
    def node_scrape_collector_duration_seconds(self, **kwargs):
        pass

    @prom
    def node_scrape_collector_success(self, **kwargs):
        pass

    @prom
    def node_sockstat_FRAG_inuse(self, **kwargs):
        pass

    @prom
    def node_sockstat_FRAG_memory(self, **kwargs):
        pass

    @prom
    def node_sockstat_RAW_inuse(self, **kwargs):
        pass

    @prom
    def node_sockstat_TCP_alloc(self, **kwargs):
        pass

    @prom
    def node_sockstat_TCP_inuse(self, **kwargs):
        pass

    @prom
    def node_sockstat_TCP_mem(self, **kwargs):
        pass

    @prom
    def node_sockstat_TCP_mem_bytes(self, **kwargs):
        pass

    @prom
    def node_sockstat_TCP_orphan(self, **kwargs):
        pass

    @prom
    def node_sockstat_TCP_tw(self, **kwargs):
        pass

    @prom
    def node_sockstat_UDPLITE_inuse(self, **kwargs):
        pass

    @prom
    def node_sockstat_UDP_inuse(self, **kwargs):
        pass

    @prom
    def node_sockstat_UDP_mem(self, **kwargs):
        pass

    @prom
    def node_sockstat_UDP_mem_bytes(self, **kwargs):
        pass

    @prom
    def node_sockstat_sockets_used(self, **kwargs):
        pass

    @prom
    def node_textfile_scrape_error(self, **kwargs):
        pass

    @prom
    def node_time(self, **kwargs):
        pass

    @prom
    def node_timex_estimated_error_seconds(self, **kwargs):
        pass

    @prom
    def node_timex_frequency_adjustment(self, **kwargs):
        pass

    @prom
    def node_timex_loop_time_constant(self, **kwargs):
        pass

    @prom
    def node_timex_maxerror_seconds(self, **kwargs):
        pass

    @prom
    def node_timex_offset_seconds(self, **kwargs):
        pass

    @prom
    def node_timex_pps_calibration_count(self, **kwargs):
        pass

    @prom
    def node_timex_pps_error_count(self, **kwargs):
        pass

    @prom
    def node_timex_pps_frequency(self, **kwargs):
        pass

    @prom
    def node_timex_pps_jitter_count(self, **kwargs):
        pass

    @prom
    def node_timex_pps_jitter_seconds(self, **kwargs):
        pass

    @prom
    def node_timex_pps_shift_seconds(self, **kwargs):
        pass

    @prom
    def node_timex_pps_stability(self, **kwargs):
        pass

    @prom
    def node_timex_pps_stability_exceeded_count(self, **kwargs):
        pass

    @prom
    def node_timex_status(self, **kwargs):
        pass

    @prom
    def node_timex_sync_status(self, **kwargs):
        pass

    @prom
    def node_timex_tai_offset(self, **kwargs):
        pass

    @prom
    def node_timex_tick_seconds(self, **kwargs):
        pass

    @prom
    def node_uname_info(self, **kwargs):
        pass

    @prom
    def node_vmstat_allocstall(self, **kwargs):
        pass

    @prom
    def node_vmstat_balloon_deflate(self, **kwargs):
        pass

    @prom
    def node_vmstat_balloon_inflate(self, **kwargs):
        pass

    @prom
    def node_vmstat_balloon_migrate(self, **kwargs):
        pass

    @prom
    def node_vmstat_compact_fail(self, **kwargs):
        pass

    @prom
    def node_vmstat_compact_free_scanned(self, **kwargs):
        pass

    @prom
    def node_vmstat_compact_isolated(self, **kwargs):
        pass

    @prom
    def node_vmstat_compact_migrate_scanned(self, **kwargs):
        pass

    @prom
    def node_vmstat_compact_stall(self, **kwargs):
        pass

    @prom
    def node_vmstat_compact_success(self, **kwargs):
        pass

    @prom
    def node_vmstat_drop_pagecache(self, **kwargs):
        pass

    @prom
    def node_vmstat_drop_slab(self, **kwargs):
        pass

    @prom
    def node_vmstat_htlb_buddy_alloc_fail(self, **kwargs):
        pass

    @prom
    def node_vmstat_htlb_buddy_alloc_success(self, **kwargs):
        pass

    @prom
    def node_vmstat_kswapd_high_wmark_hit_quickly(self, **kwargs):
        pass

    @prom
    def node_vmstat_kswapd_inodesteal(self, **kwargs):
        pass

    @prom
    def node_vmstat_kswapd_low_wmark_hit_quickly(self, **kwargs):
        pass

    @prom
    def node_vmstat_nr_active_anon(self, **kwargs):
        pass

    @prom
    def node_vmstat_nr_active_file(self, **kwargs):
        pass

    @prom
    def node_vmstat_nr_alloc_batch(self, **kwargs):
        pass

    @prom
    def node_vmstat_nr_anon_pages(self, **kwargs):
        pass

    @prom
    def node_vmstat_nr_anon_transparent_hugepages(self, **kwargs):
        pass

    @prom
    def node_vmstat_nr_bounce(self, **kwargs):
        pass

    @prom
    def node_vmstat_nr_dirtied(self, **kwargs):
        pass

    @prom
    def node_vmstat_nr_dirty(self, **kwargs):
        pass

    @prom
    def node_vmstat_nr_dirty_background_threshold(self, **kwargs):
        pass

    @prom
    def node_vmstat_nr_dirty_threshold(self, **kwargs):
        pass

    @prom
    def node_vmstat_nr_file_pages(self, **kwargs):
        pass

    @prom
    def node_vmstat_nr_free_cma(self, **kwargs):
        pass

    @prom
    def node_vmstat_nr_free_pages(self, **kwargs):
        pass

    @prom
    def node_vmstat_nr_inactive_anon(self, **kwargs):
        pass

    @prom
    def node_vmstat_nr_inactive_file(self, **kwargs):
        pass

    @prom
    def node_vmstat_nr_isolated_anon(self, **kwargs):
        pass

    @prom
    def node_vmstat_nr_isolated_file(self, **kwargs):
        pass

    @prom
    def node_vmstat_nr_kernel_stack(self, **kwargs):
        pass

    @prom
    def node_vmstat_nr_mapped(self, **kwargs):
        pass

    @prom
    def node_vmstat_nr_mlock(self, **kwargs):
        pass

    @prom
    def node_vmstat_nr_page_table_pages(self, **kwargs):
        pass

    @prom
    def node_vmstat_nr_pages_scanned(self, **kwargs):
        pass

    @prom
    def node_vmstat_nr_shmem(self, **kwargs):
        pass

    @prom
    def node_vmstat_nr_slab_reclaimable(self, **kwargs):
        pass

    @prom
    def node_vmstat_nr_slab_unreclaimable(self, **kwargs):
        pass

    @prom
    def node_vmstat_nr_unevictable(self, **kwargs):
        pass

    @prom
    def node_vmstat_nr_unstable(self, **kwargs):
        pass

    @prom
    def node_vmstat_nr_vmscan_immediate_reclaim(self, **kwargs):
        pass

    @prom
    def node_vmstat_nr_vmscan_write(self, **kwargs):
        pass

    @prom
    def node_vmstat_nr_writeback(self, **kwargs):
        pass

    @prom
    def node_vmstat_nr_writeback_temp(self, **kwargs):
        pass

    @prom
    def node_vmstat_nr_written(self, **kwargs):
        pass

    @prom
    def node_vmstat_numa_foreign(self, **kwargs):
        pass

    @prom
    def node_vmstat_numa_hint_faults(self, **kwargs):
        pass

    @prom
    def node_vmstat_numa_hint_faults_local(self, **kwargs):
        pass

    @prom
    def node_vmstat_numa_hit(self, **kwargs):
        pass

    @prom
    def node_vmstat_numa_huge_pte_updates(self, **kwargs):
        pass

    @prom
    def node_vmstat_numa_interleave(self, **kwargs):
        pass

    @prom
    def node_vmstat_numa_local(self, **kwargs):
        pass

    @prom
    def node_vmstat_numa_miss(self, **kwargs):
        pass

    @prom
    def node_vmstat_numa_other(self, **kwargs):
        pass

    @prom
    def node_vmstat_numa_pages_migrated(self, **kwargs):
        pass

    @prom
    def node_vmstat_numa_pte_updates(self, **kwargs):
        pass

    @prom
    def node_vmstat_pageoutrun(self, **kwargs):
        pass

    @prom
    def node_vmstat_pgactivate(self, **kwargs):
        pass

    @prom
    def node_vmstat_pgalloc_dma(self, **kwargs):
        pass

    @prom
    def node_vmstat_pgalloc_dma32(self, **kwargs):
        pass

    @prom
    def node_vmstat_pgalloc_movable(self, **kwargs):
        pass

    @prom
    def node_vmstat_pgalloc_normal(self, **kwargs):
        pass

    @prom
    def node_vmstat_pgdeactivate(self, **kwargs):
        pass

    @prom
    def node_vmstat_pgfault(self, **kwargs):
        pass

    @prom
    def node_vmstat_pgfree(self, **kwargs):
        pass

    @prom
    def node_vmstat_pginodesteal(self, **kwargs):
        pass

    @prom
    def node_vmstat_pgmajfault(self, **kwargs):
        pass

    @prom
    def node_vmstat_pgmigrate_fail(self, **kwargs):
        pass

    @prom
    def node_vmstat_pgmigrate_success(self, **kwargs):
        pass

    @prom
    def node_vmstat_pgpgin(self, **kwargs):
        pass

    @prom
    def node_vmstat_pgpgout(self, **kwargs):
        pass

    @prom
    def node_vmstat_pgrefill_dma(self, **kwargs):
        pass

    @prom
    def node_vmstat_pgrefill_dma32(self, **kwargs):
        pass

    @prom
    def node_vmstat_pgrefill_movable(self, **kwargs):
        pass

    @prom
    def node_vmstat_pgrefill_normal(self, **kwargs):
        pass

    @prom
    def node_vmstat_pgrotated(self, **kwargs):
        pass

    @prom
    def node_vmstat_pgscan_direct_dma(self, **kwargs):
        pass

    @prom
    def node_vmstat_pgscan_direct_dma32(self, **kwargs):
        pass

    @prom
    def node_vmstat_pgscan_direct_movable(self, **kwargs):
        pass

    @prom
    def node_vmstat_pgscan_direct_normal(self, **kwargs):
        pass

    @prom
    def node_vmstat_pgscan_direct_throttle(self, **kwargs):
        pass

    @prom
    def node_vmstat_pgscan_kswapd_dma(self, **kwargs):
        pass

    @prom
    def node_vmstat_pgscan_kswapd_dma32(self, **kwargs):
        pass

    @prom
    def node_vmstat_pgscan_kswapd_movable(self, **kwargs):
        pass

    @prom
    def node_vmstat_pgscan_kswapd_normal(self, **kwargs):
        pass

    @prom
    def node_vmstat_pgsteal_direct_dma(self, **kwargs):
        pass

    @prom
    def node_vmstat_pgsteal_direct_dma32(self, **kwargs):
        pass

    @prom
    def node_vmstat_pgsteal_direct_movable(self, **kwargs):
        pass

    @prom
    def node_vmstat_pgsteal_direct_normal(self, **kwargs):
        pass

    @prom
    def node_vmstat_pgsteal_kswapd_dma(self, **kwargs):
        pass

    @prom
    def node_vmstat_pgsteal_kswapd_dma32(self, **kwargs):
        pass

    @prom
    def node_vmstat_pgsteal_kswapd_movable(self, **kwargs):
        pass

    @prom
    def node_vmstat_pgsteal_kswapd_normal(self, **kwargs):
        pass

    @prom
    def node_vmstat_pswpin(self, **kwargs):
        pass

    @prom
    def node_vmstat_pswpout(self, **kwargs):
        pass

    @prom
    def node_vmstat_slabs_scanned(self, **kwargs):
        pass

    @prom
    def node_vmstat_thp_collapse_alloc(self, **kwargs):
        pass

    @prom
    def node_vmstat_thp_collapse_alloc_failed(self, **kwargs):
        pass

    @prom
    def node_vmstat_thp_fault_alloc(self, **kwargs):
        pass

    @prom
    def node_vmstat_thp_fault_fallback(self, **kwargs):
        pass

    @prom
    def node_vmstat_thp_split(self, **kwargs):
        pass

    @prom
    def node_vmstat_thp_zero_page_alloc(self, **kwargs):
        pass

    @prom
    def node_vmstat_thp_zero_page_alloc_failed(self, **kwargs):
        pass

    @prom
    def node_vmstat_unevictable_pgs_cleared(self, **kwargs):
        pass

    @prom
    def node_vmstat_unevictable_pgs_culled(self, **kwargs):
        pass

    @prom
    def node_vmstat_unevictable_pgs_mlocked(self, **kwargs):
        pass

    @prom
    def node_vmstat_unevictable_pgs_munlocked(self, **kwargs):
        pass

    @prom
    def node_vmstat_unevictable_pgs_rescued(self, **kwargs):
        pass

    @prom
    def node_vmstat_unevictable_pgs_scanned(self, **kwargs):
        pass

    @prom
    def node_vmstat_unevictable_pgs_stranded(self, **kwargs):
        pass

    @prom
    def node_vmstat_workingset_activate(self, **kwargs):
        pass

    @prom
    def node_vmstat_workingset_nodereclaim(self, **kwargs):
        pass

    @prom
    def node_vmstat_workingset_refault(self, **kwargs):
        pass

    @prom
    def node_vmstat_zone_reclaim_failed(self, **kwargs):
        pass

    @prom
    def node_wifi_interface_frequency_hertz(self, **kwargs):
        pass

    @prom
    def node_wifi_station_beacon_loss_total(self, **kwargs):
        pass

    @prom
    def node_wifi_station_connected_seconds_total(self, **kwargs):
        pass

    @prom
    def node_wifi_station_inactive_seconds(self, **kwargs):
        pass

    @prom
    def node_wifi_station_info(self, **kwargs):
        pass

    @prom
    def node_wifi_station_receive_bits_per_second(self, **kwargs):
        pass

    @prom
    def node_wifi_station_signal_dbm(self, **kwargs):
        pass

    @prom
    def node_wifi_station_transmit_bits_per_second(self, **kwargs):
        pass

    @prom
    def node_wifi_station_transmit_failed_total(self, **kwargs):
        pass

    @prom
    def node_wifi_station_transmit_retries_total(self, **kwargs):
        pass

    @relabel('100 - (avg by (instance, job) (irate(node_cpu{mode="idle"}[5m])) * 100)')
    def node_cpu_rate(self, **kwargs):
        pass

    @relabel(
        '(node_filesystem_size{} - node_filesystem_free{})'
        ' / (node_filesystem_size{} - node_filesystem_free{} + node_filesystem_avail{})'
        ' * 100')
    def node_disk_rate(self, **kwargs):
        pass

    @relabel('100 * (node_memory_MemTotal{} - node_memory_MemFree{}) / node_memory_MemTotal{}')
    def node_memory_rate(self, **kwargs):
        pass

    @relabel('irate(node_network_transmit_bytes_total{}[5m])')
    def node_network_transmit_rate(self, **kwargs):
        pass

    @relabel('irate(node_network_receive_bytes_total{}[5m])')
    def node_network_receive_rate(self, **kwargs):
        pass
