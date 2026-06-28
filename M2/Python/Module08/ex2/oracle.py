import os
import sys
from dotenv import load_dotenv


load_dotenv()  # abre el archivo .env y carga sus variables

# Obtener variables
matrix_mode = os.getenv("MATRIX_MODE")  # busca una variable llamada...
database_url = os.getenv("DATABASE_URL")
api_key = os.getenv("API_KEY")
log_level = os.getenv("LOG_LEVEL")
zion_endpoint = os.getenv("ZION_ENDPOINT")

# Verificar que existan
required_vars = {
    "MATRIX_MODE": matrix_mode,
    "DATABASE_URL": database_url,
    "API_KEY": api_key,
    "LOG_LEVEL": log_level,
    "ZION_ENDPOINT": zion_endpoint
}

missing = []

for key, value in required_vars.items():
    if value is None or value.strip() == "":
        missing.append(key)

if missing:
    print("Error: Missing configuration variables:")

    for var in missing:
        print(f" - {var}")

    sys.exit(1)


# Mostrar configuración
print("\nORACLE STATUS: Reading the Matrix...\n")
if matrix_mode == "development":
    print("[DEVELOPMENT MODE]")
    print(f"Mode: {matrix_mode}")
    print("Debugging is enabled.")
    print(f"API Key: {api_key}")
    print(f"Log Level: {log_level}")

elif matrix_mode == "production":
    print("[PRODUCTION MODE]")
    print(f"Mode: {matrix_mode}")
    print("Debugging is disabled.")
    print("API Key: [HIDDEN]")

else:
    print("WARNING: Unknown MATRIX_MODE")

print(f"Database: {database_url}")
print(f"Zion Endpoint: {zion_endpoint}")

# Diferencia development/production
"""
En development

Quieres:

ver errores
mostrar información
hacer pruebas
"""

"""
En production

Quieres:

seguridad
ocultar secretos
estabilidad
"""
