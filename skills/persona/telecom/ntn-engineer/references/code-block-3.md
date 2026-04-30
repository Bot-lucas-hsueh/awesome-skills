# python Example

```
def tcp_ntn_optimization(RTT_ms, bandwidth_bps, packet_loss_rate=0.001):
    """
    TCP throughput calculation over NTN link.
    Problem: standard TCP window size insufficient for large BDP.
    BDP (Bandwidth-Delay Product) = bandwidth × RTT
    Required TCP window ≥ BDP for full throughput utilization.
    """
    RTT_s = RTT_ms

    # Bandwidth-Delay Product
    BDP_bits = bandwidth_bps * RTT_s
    BDP_bytes = BDP_bits
    BDP_KB = BDP_bytes

    # Standard TCP max window: 64 KB (16-bit window field)
    # TCP window scaling (RFC 7323): up to 1 GB window
    tcp_throughput_standard = min(64 * 1024 * 8, BDP_bits) / RTT_s  # bits/s
    tcp_throughput_optimal = BDP_bits

    # Mathis formula: throughput = MSS/(RTT * sqrt(p))
    MSS = 1460  # bytes (standard TCP MSS)
    tcp_throughput_mathis = MSS * 8

    return {
        'RTT_ms': RTT_ms,
        'BDP_MB': round(BDP_bytes
        'tcp_standard_Mbps': round(tcp_throughput_standard
        'tcp_optimal_Mbps': round(tcp_throughput_optimal
        'tcp_mathis_Mbps': round(tcp_throughput_mathis
        'window_required_MB': round(BDP_bytes
        'recommendation': 'Use TCP window scaling (RFC 7323) + BBR congestion control OR QUIC'
            if BDP_bytes > 64 * 1024 else 'Standard TCP sufficient',
    }

# LEO 600 km at 10° elevation: RTT = 28 ms (round trip)
result = tcp_ntn_optimization(RTT_ms=28, bandwidth_bps=50e6, packet_loss_rate=0.001)
print(f"LEO TCP: BDP={result['BDP_MB']} MB, Standard TCP: {result['tcp_standard_Mbps']} Mbps, "
      f"Optimal: {result['tcp_optimal_Mbps']} Mbps")

# GEO: RTT = 550 ms
result_geo = tcp_ntn_optimization(RTT_ms=550, bandwidth_bps=50e6, packet_loss_rate=0.001)
print(f"GEO TCP: BDP={result_geo['BDP_MB']} MB, Standard TCP: {result_geo['tcp_standard_Mbps']} Mbps")
# GEO: BDP = 3.44 MB, Standard TCP throughput: ~0.93 Mbps vs 50 Mbps available — 98% waste!
# → MANDATORY: TCP window scaling OR switch to QUIC (connection migration, multipath)
```
