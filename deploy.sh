#!/bin/bash

# Nombre del archivo de llave privada para acceder a la instancia EC2
KEY_PAIR="keypair-testing.pem"

# Dirección IP pública de la instancia EC2
PUBLIC_IP="18.236.187.67"

# Nombre del usuario para acceder a la instancia EC2 (puede variar según la AMI)
USER="ubuntu"


# Ruta local del archivo que deseas copiar a la instancia EC2
LOCAL_FOLDER="./app"

# Ruta en la instancia EC2 donde deseas copiar el archivo
REMOTE_FOLDER="/app"

# Crear la carpeta /app en la instancia EC2
echo "Creando la carpeta /app en la instancia EC2..."
ssh -i $KEY_PAIR $USER@$PUBLIC_IP "sudo mkdir -p $REMOTE_FOLDER"

# Copiar el archivo desde tu máquina local a la instancia EC2
echo "Copiando el archivo a la carpeta /app en la instancia EC2..."
scp -i $KEY_PAIR -r $LOCAL_FOLDER/* $USER@$PUBLIC_IP:/tmp/
ssh -i $KEY_PAIR $USER@$PUBLIC_IP "sudo mv /tmp/* $REMOTE_FOLDER/ && sudo chown -R $USER:$USER $REMOTE_FOLDER"
ssh -i $KEY_PAIR $USER@$PUBLIC_IP "cd /app && sudo apt-get update && sudo apt-get install -y python3-pip python3-venv && python3 -m venv myenv && source myenv/bin/activate && pip install Flask Pillow PyYAML boto3 && flask --app main run --host=0.0.0.0"

echo "El archivo se ha copiado correctamente en la carpeta /app en la instancia EC2."

echo "Proceso completo."
