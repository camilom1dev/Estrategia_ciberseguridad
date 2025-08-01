#!/usr/bin/env python3

import subprocess
import datetime
import os

fecha = datetime.date.today().isoformat()
log_dir = "/var/log/clininova_auditoria"
log_file = f"{log_dir}/auditoria_{fecha}.log"

# Crear directorio si no existe
os.makedirs(log_dir, exist_ok=True)

print(f"[INFO] Ejecutando auditoría para {fecha}...")

try:
    with open(log_file, "w") as f:
        result = subprocess.run(
            ["ausearch", "-ts", fecha, "-m", "EXECVE,USER_LOGIN,USER_START,USER_END,AVC"],
            stdout=f,
            stderr=subprocess.STDOUT
        )
    print(f"[OK] Auditoría finalizada. Resultado en: {log_file}")
except Exception as e:
    print(f"[ERROR] Falló la auditoría: {e}")
