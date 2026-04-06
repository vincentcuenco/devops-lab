#!/usr/bin/env python3
import socket

servers = [
    {"name": "grafanaserver", "ip": "192.168.7.85", "port": 3000},
    {"name": "prometheus", "ip": "192.168.7.85", "port": 9090},
    {"name": "blackbox", "ip": "192.168.7.85", "port": 9115},
]

def check_port(ip, port, timeout=3):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0  # True = open, False = closed
    except:
        return False

for server in servers:
    status = check_port(server["ip"], server["port"])
    icon = "✅" if status else "❌"
    print(f"{icon} {server['name']} | {server['ip']}:{server['port']}")
