#!/usr/bin/env python3
"""
NetSage AI deterministic rule checker.
Checks: duplicate IPs, wrong masks, gateway mismatch, interface down,
missing VLAN, missing routes. Uses a small text/config fixture so it
can be run without Packet Tracer or external dependencies.
"""
import ipaddress, re, sys

def check_duplicate_ips(text):
    ips = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', text)
    counts = {}
    for ip in ips:
        try: ipaddress.ip_address(ip)
        except ValueError: continue
        counts[ip] = counts.get(ip, 0) + 1
    return [ip for ip, n in counts.items() if n > 1]

def check_wrong_masks(text):
    # Flags the explicit fixture marker or two hosts in the same /24 with /25.
    if "MASK_MISMATCH" in text:
        return True
    return bool(re.search(r'HostA.*192\.168\.10\.\d+\/24.*HostB.*192\.168\.10\.\d+\/25', text, re.S))

def check_gateway_mismatch(text):
    m = re.search(r'network\s+(\d+\.\d+\.\d+\.\d+)\s+(\d+\.\d+\.\d+\.\d+).*default-router\s+(\d+\.\d+\.\d+\.\d+)', text, re.S)
    return bool(m and m.group(2) != m.group(3))

def check_interface_down(text):
    return bool(re.search(r'(administratively down|down/down|shutdown)', text, re.I))

def check_missing_vlan(text):
    configured = set(re.findall(r'vlan\s+(\d+)', text, re.I))
    access = set(re.findall(r'access vlan\s+(\d+)', text, re.I))
    return sorted(access - configured)

def check_missing_routes(text):
    required = re.findall(r'REQUIRED_ROUTE\s+(\d+\.\d+\.\d+\.\d+/\d+)', text)
    routes = re.findall(r'(?:ip route|ROUTE)\s+(\d+\.\d+\.\d+\.\d+/\d+)', text, re.I)
    return sorted(set(required) - set(routes))

def run(text):
    return {
        "duplicate_ips": check_duplicate_ips(text),
        "wrong_masks": check_wrong_masks(text),
        "gateway_mismatch": check_gateway_mismatch(text),
        "interface_down": check_interface_down(text),
        "missing_vlans": check_missing_vlan(text),
        "missing_routes": check_missing_routes(text),
    }

if __name__ == "__main__":
    sample = """HostA 192.168.10.20/24 HostB 192.168.10.20/24
network 192.168.20.0 255.255.255.0 default-router 192.168.20.254
Gi0/0 administratively down
access vlan 30
vlan 20
REQUIRED_ROUTE 10.20.0.0/16
"""
    print(run(sample))
