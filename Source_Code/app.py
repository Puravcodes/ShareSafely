from flask import Flask, request, redirect, url_for, render_template
from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions
from datetime import datetime, timedelta
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import os

app = Flask(__name__)

# Configuration - Using environment variables for security
KEY_VAULT_NAME = os.getenv('KEY_VAULT_NAME', 'keyvaultsharesafely')
STORAGE_ACCOUNT_NAME = os.getenv('STORAGE_ACCOUNT_NAME', 'sharesafelyblob')
CONTAINER_NAME = os.getenv('CONTAINER_NAME', 'uploads')
SECRET_NAME = os.getenv('SECRET_NAME', 'sharesafely-secret-key')  # The name of the secret in Key Vault

# Construct the Key Vault URL
key_vault_url = f"https://{KEY_VAULT_NAME}.vault.azure.net"

try:
    # Initialize credentials and clients
    credential = DefaultAzureCredential()
    secret_client = SecretClient(vault_url=key_vault_url, credential=credential)
    
    # Fetch the ACCOUNT_KEY from Key Vault
    secret = secret_client.get_secret(SECRET_NAME)
    ACCOUNT_KEY = secret.value
    
    # Construct connection string
    connection_string = (
    f"DefaultEndpointsProtocol=https;"
    f"AccountName={STORAGE_ACCOUNT_NAME};"
    f"AccountKey={ACCOUNT_KEY};"
    f"EndpointSuffix=core.windows.net"
    )
    
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

except Exception as e:
    print(f"Error during setup: {e}")

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files.get('file')
        if file and file.filename:  # Ensure the file is valid and has a filename
            try:
                blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=file.filename)
                blob_client.upload_blob(file, overwrite=True)
                
                # Generate SAS Token
                sas_token = generate_blob_sas(
                    account_name=STORAGE_ACCOUNT_NAME,
                    container_name=CONTAINER_NAME,
                    blob_name=file.filename,
                    account_key= ACCOUNT_KEY, #Input the account key here 
                    expiry=datetime.utcnow() + timedelta(seconds=15)  # Adjust time as needed
                )
                sas_url = f"https://{STORAGE_ACCOUNT_NAME}.blob.core.windows.net/{CONTAINER_NAME}/{file.filename}?{sas_token}"
                return redirect(url_for('file_link', url=sas_url))
            except Exception as e:
                print(f"Error uploading file or generating SAS token: {e}")
    return render_template('upload.html')

@app.route('/link')
def file_link():
    url = request.args.get('url')
    return render_template('upload-link.html', url=url)

if __name__ == '__main__':
    app.run(debug=True)







