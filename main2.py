from pymodbus.client import ModbusTcpClient
import logging
import time

# Configurar logs opcionalmente
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.WARNING)

# Parámetros
MODBUS_SERVER_IP = '192.168.1.100'  # Cambia por la IP real
MODBUS_PORT = 502
UNIT_ID = 1
ADDRESS = 0
COUNT = 10
INTERVAL_SECONDS = 2

# Crear cliente
client = ModbusTcpClient(host=MODBUS_SERVER_IP, port=MODBUS_PORT)

try:
    connection = client.connect()
    if connection:
        print("✅ Conectado exitosamente al servidor Modbus")

        while True:
            result = client.read_holding_registers(address=ADDRESS, count=COUNT, unit=UNIT_ID)

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
