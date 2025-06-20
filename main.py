from pymodbus.client.sync import ModbusTcpClient
import logging
import time

# Configura los logs de la librería (opcional)
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.WARNING)  # Usa DEBUG si quieres ver toda la comunicación

# Parámetros de conexión
MODBUS_SERVER_IP = '192.168.1.100'  # Cambia a la IP de tu dispositivo
MODBUS_PORT = 502
UNIT_ID = 1
ADDRESS = 0
COUNT = 10
INTERVAL_SECONDS = 2

# Crear cliente
client = ModbusTcpClient(MODBUS_SERVER_IP, port=MODBUS_PORT)

try:
    if client.connect():
        print("✅ Conectado exitosamente al servidor Modbus")

        while True:
            # Leer registros holding
            result = client.read_holding_registers(ADDRESS, COUNT, unit=UNIT_ID)

            if not result.isError():
                print(f"📥 Registros leídos: {result.registers}")
            else:
                print(f"⚠️ Error al leer registros: {result}")

            time.sleep(INTERVAL_SECONDS)

    else:
        print("❌ No se pudo conectar al servidor Modbus")

except KeyboardInterrupt:
    print("\n⏹️ Lectura detenida por el usuario")

finally:
    client.close()
    print("🔌 Conexión cerrada")
