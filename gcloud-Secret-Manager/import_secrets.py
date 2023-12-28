from google.cloud import secretmanager
from dotenv import load_dotenv

# Carga variables de entorno desde el archivo .env si está presente
load_dotenv()

# ID del proyecto de Google Cloud (reemplazar con el proyecto correcto)
PROJECT_ID = "tu-proyecto-de-google-cloud"

# Función para listar y mostrar valores de secretos
def list_secrets(project_id):
    # Crea una instancia del cliente de Google Cloud Secret Manager
    client = secretmanager.SecretManagerServiceClient()

    # Define la ruta del proyecto para listar secretos
    parent = f"projects/{project_id}"

    # Obtiene la lista de secretos en el proyecto
    secrets = client.list_secrets(request={"parent": parent})

    # Itera sobre los secretos y muestra sus nombres y valores
    for secret in secrets:
        print(f"Secreto: {secret.name}")
        
        # Obtiene la versión más reciente del secreto y su valor decodificado
        version = client.access_secret_version(request={"name": f"{secret.name}/versions/latest"})
        value = version.payload.data.decode("utf-8")
        
        print(f"Valor: {value}")
        print("------------------------")

# Función principal
if __name__ == '__main__':
    # Llama a la función para listar secretos en el proyecto dado
    list_secrets(PROJECT_ID)
