#!/usr/bin/env python3

import subprocess

# Reglas de Zero Trust entre VLANs
reglas = [
    ["iptables", "-A", "FORWARD", "-s", "192.168.10.0/24", "-d", "192.168.20.0/24", "-j", "DROP"],
    ["iptables", "-A", "FORWARD", "-s", "192.168.20.0/24", "-d", "192.168.10.0/24", "-j", "DROP"],
    ["iptables", "-A", "FORWARD", "-s", "192.168.10.0/24", "-d", "192.168.30.10", "-p", "tcp", "--dport", "443", "-j", "ACCEPT"],
    ["iptables", "-A", "FORWARD", "-j", "DROP"]
]

print("[INFO] Aplicando reglas de segmentación Zero Trust...")

for regla in reglas:
    try:
        subprocess.run(regla, check=True)
        print(f"[OK] Regla aplicada: {' '.join(regla)}")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] No se pudo aplicar la regla: {' '.join(regla)}")

print("[COMPLETADO] Segmentación aplicada.")
