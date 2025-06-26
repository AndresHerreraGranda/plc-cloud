from pymodbus.client import ModbusTcpClient
from supabase import create_client, Client
import logging
import time
from datetime import datetime

# Parámetros Modbus
MODBUS_SERVER_IP = '192.168.1.100'
MODBUS_PORT = 502
UNIT_ID = 1
ADDRESS = 0
COUNT = 10
INTERVAL_SECONDS = 5

# Supabase configuración
SUPABASE_URL = "https://jzsmavfiptmpjaxarbhc.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imp6c21hdmZpcHRtcGpheGFyYmhjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTA5NjAxODEsImV4cCI6MjA2NjUzNjE4MX0.u38v2fHOfpHFpo0L14Tn5RJvzxR6-sZ0DmRDKLTHtx" 
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Configurar logs
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.WARNING)

# Crear cliente Modbus
client = ModbusTcpClient(host=MODBUS_SERVER_IP, port=MODBUS_PORT)

try:
    if client.connect():
        print("✅ Conectado exitosamente al servidor Modbus")

        while True:
            result = client.read_holding_registers(address=ADDRESS, count=COUNT, unit=UNIT_ID)

            if not result.isError():
                registros = result.registers
                print(f"📥 Registros leídos: {registros}")

                # Preparar datos para Supabase
                data = {
                    "reg0": registros[0],
                    "reg1": registros[1],
                    "reg2": registros[2],
                    "reg3": registros[3],
                    "reg4": registros[4],
                    "reg5": registros[5],
                    "reg6": registros[6],
                    "reg7": registros[7],
                    "reg8": registros[8],
                    "reg9": registros[9],
                    "timestamp": datetime.utcnow().isoformat()
                }

                # Insertar en Supabase
                response = supabase.table("modbus_data").insert(data).execute()
                print("⬆️ Datos enviados a Supabase:", response)

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
