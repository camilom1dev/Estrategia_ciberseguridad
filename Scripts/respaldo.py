#!/usr/bin/env python3

import os
import datetime
import tarfile
import boto3
from botocore.exceptions import BotoCoreError, ClientError

# Variables
src_dir = "/var/www/html/historias_clinicas"
date_str = datetime.date.today().isoformat()
tar_path = f"/tmp/respaldo_{date_str}.tar.gz"
bucket_name = "clininova-respaldos"
s3_key = f"respaldos/respaldo_{date_str}.tar.gz"

# Crear archivo .tar.gz
def crear_respaldo(origen, destino):
    with tarfile.open(destino, "w:gz") as tar:
        tar.add(origen, arcname=os.path.basename(origen))

try:
    print("[INFO] Generando archivo comprimido...")
    crear_respaldo(src_dir, tar_path)
    print(f"[OK] Respaldo creado en {tar_path}")
except Exception as e:
    print(f"[ERROR] Error al crear respaldo: {e}")
    exit(1)

# Subir a S3
s3 = boto3.client('s3')

try:
    print("[INFO] Subiendo a S3...")
    s3.upload_file(tar_path, bucket_name, s3_key)
    print(f"[OK] Respaldo subido exitosamente a s3://{bucket_name}/{s3_key}")
except (BotoCoreError, ClientError) as e:
    print(f"[ERROR] Error al subir a S3: {e}")

# Limpieza
try:
    os.remove(tar_path)
    print("[INFO] Archivo temporal eliminado.")
except Exception as e:
    print(f"[WARN] No se pudo borrar archivo temporal: {e}")
