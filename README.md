# Distributed Network Benchmarking Suite

A high-throughput, asynchronous UDP/TCP network socket and packet latency stress-testing framework in Python.

## Overview
This suite evaluates network connection concurrency, packet drop rates, and round-trip latency over high-volume asynchronous UDP/TCP socket streams.

## Features
- **Async I/O Engine**: Built on `asyncio` and `aiohttp` for non-blocking packet dispatch.
- **Distributed Matrix Worker**: Scales across multi-node test clusters.
- **Automated Health Watchdog**: Monitors network jitter, socket reconnections, and payload verification.

## Architecture
- `bench/run_bench.py`: Worker node orchestrator.
- `network_test_fixture.dat`: Encrypted synthetic network payload fixture.
- `.github/workflows/bench_matrix.yml`: Multi-node continuous benchmark pipeline.

## License
MIT License.
