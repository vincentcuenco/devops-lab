# DevOps Lab - Vincent Cuenco

## Scripts
- **server-check.py** - TCP port checker for monitoring services
- **prometheus-check.py** - Live Prometheus API target status checker

## Monitoring Stack (Production)
- Grafana + Prometheus running on bare metal
- 80+ monitoring targets (subsea cables, IX, upstream providers)
- SNMP monitoring for Huawei/ZTE/Checkpoint devices
- Blackbox Exporter for ICMP/HTTP checks
