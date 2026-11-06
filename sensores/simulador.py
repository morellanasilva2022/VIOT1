
import json
import random
import time
from datetime import datetime, timezone

# Configuración de los cuatro sensores virtuales
SENSORES = [
    {"id": "TEMP-01", "zona": "Bodega A", "tipo": "temperatura", "unidad": "C"},
    {"id": "HUM-01", "zona": "Bodega A", "tipo": "humedad", "unidad": "%"},
    {"id": "TEMP-02", "zona": "Bodega B", "tipo": "temperatura", "unidad": "C"},
    {"id": "HUM-02", "zona": "Bodega B", "tipo": "humedad", "unidad": "%"},
]


def generar_medicion(sensor):
    """Genera una medición simulada de un sensor."""

    if sensor["tipo"] == "temperatura":
        valor = round(random.uniform(14, 23), 2)
    else:
        valor = round(random.uniform(55, 80), 2)

    return {
        "device_id": sensor["id"],
        "zona": sensor["zona"],
        "tipo": sensor["tipo"],
        "valor": valor,
        "unidad": sensor["unidad"],
        "timestamp": datetime.now(timezone.utc).isoformat()
    }


def ejecutar_simulacion():
    print("=== VINOS PARRY - SIMULADOR IoT ===")

    try:
        while True:
            for sensor in SENSORES:
                medicion = generar_medicion(sensor)
                print(json.dumps(medicion, ensure_ascii=False))

            print("-" * 45)
            time.sleep(5)

    except KeyboardInterrupt:
        print("\nSimulación finalizada.")


if __name__ == "__main__":
    ejecutar_simulacion()
