#!/usr/bin/env python3
import requests

PROMETHEUS_URL = "http://192.168.7.85:9090"

def check_targets():
    try:
        response = requests.get(
            f"{PROMETHEUS_URL}/api/v1/query",
            params={"query": "up"},
            timeout=5
        )
        data = response.json()

        print("=== Prometheus Targets Status ===")
        for result in data["data"]["result"]:
            job = result["metric"].get("job", "unknown")
            instance = result["metric"].get("instance", "unknown")
            status = "✅ UP" if result["value"][1] == "1" else "❌ DOWN"
            print(f"{status} | {job} | {instance}")

    except Exception as e:
        print(f"Error: {e}")

check_targets()
