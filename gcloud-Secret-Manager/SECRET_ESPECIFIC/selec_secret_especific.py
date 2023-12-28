from typing import Final
from google.cloud import secretmanager
from dotenv import load_dotenv

# Carga variables de entorno desde el archivo .env si está presente
load_dotenv()

# Definición de constantes para IDs de secretos y formato de decodificación
SECRET_CERTS_ID: Final = "certs"
SECRET_SECRETO_ID: Final = "secreto"
DECODE_FORMAT: Final = "utf-8"

# ID del proyecto de Google Cloud (reemplazar con el proyecto correcto)
PROJECT_ID = "tu-proyecto-de-google-cloud"

# Función para construir el nombre del secreto
def get_name(project_id, secret_id, version):
    return f"projects/{project_id}/secrets/{secret_id}/versions/{version}"

# Función para obtener el valor de un secreto
def get_secret(project_id, secret_id, version="latest"):
    name = get_name(project_id, secret_id, version)
    client = secretmanager.SecretManagerServiceClient()
    response = client.access_secret_version(request={"name": name})
    payload = response.payload.data.decode(DECODE_FORMAT)
    return payload

# Función principal
if __name__ == '__main__':
    # Llama a la función para obtener y mostrar el valor del secreto "certs"
    print(get_secret(PROJECT_ID, SECRET_CERTS_ID))

    # Llama a la función para obtener y mostrar el valor del secreto "secreto"
    print(get_secret(PROJECT_ID, SECRET_SECRETO_ID))
