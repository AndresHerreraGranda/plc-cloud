from pymodbus.client.sync import ModbusTcpClient
import time

# Configura la IP y el puerto del servidor Modbus TCP (Windows)
MODBUS_SERVER_IP = '192.168.1.50'  # Cambia esto por la IP real de tu máquina Windows
MODBUS_PORT = 502  # Usa 1502 si configuraste un puerto alternativo
UNIT_ID = 1        # ID del esclavo (usualmente 1 por defecto)
ADDRESS = 0        # Dirección inicial del registro a leer
COUNT = 10         # Cuántos registros leer
INTERVAL_SECONDS = 2

# Crear el cliente Modbus
client = ModbusTcpClient(MODBUS_SERVER_IP, port=MODBUS_PORT, timeout=3)

try:
    if client.connect():
        print(f"✅ Conectado a {MODBUS_SERVER_IP}:{MODBUS_PORT} correctamente")

        while True:
            # Leer registros holding
            result = client.read_holding_registers(ADDRESS, COUNT, unit=UNIT_ID)

            if not result.isError():
                print(f"📥 Registros leídos desde dirección {ADDRESS}: {result.registers}")
            else:
                print(f"⚠️ Error al leer registros: {result}")

            time.sleep(INTERVAL_SECONDS)

    else:
        print(f"❌ No se pudo conectar al servidor Modbus en {MODBUS_SERVER_IP}:{MODBUS_PORT}")

except KeyboardInterrupt:
    print("\n⏹️ Lectura interrumpida por el usuario")

finally:
    client.close()
    print("🔌 Conexión cerrada")
