import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Entrada
    bucket_name = event["body"]["bucket_name"]
    folder_name = event["body"]["folder_name"]

    # Proceso
    if not folder_name.endswith("/"):
        folder_name += "/"

    try:
        s3.put_object(Bucket=bucket_name, Key=folder_name)
        return {"status": "ok", "message": f"Directorio '{folder_name}' creado en {bucket_name}"}
    except Exception as e:
        return {"status": "error", "error": str(e)}
