import boto3
import base64

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Entrada
    bucket_name = event["body"]["bucket_name"]
    folder_name = event["body"]["folder_name"]
    file_name = event["body"]["file_name"]
    file_content_base64 = ["body"]["file_content"]

    # Proceso
    # Convertir el archivo desde base64
    file_bytes = base64.b64decode(file_content_base64)
    key = folder_name + file_name

    try:
        s3.put_object(Bucket=bucket_name, Key=key, Body=file_bytes)
        return {"status": "ok", "message": f"Archivo '{file_name}' subido a 's3://{bucket_name}/{key}'"}
    except Exception as e:
        return {"status": "error", "error": str(e)}
