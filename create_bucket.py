import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Entrada 
    bucket_name = event['body']['bucket_name']
    region = event['body']['region']

    # Proceso
    try:
        if region == "us-east-1":
            s3.create_bucket(Bucket=bucket_name)
        else:
            s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region}
            )
        return {"status": "ok", "message": f"Bucket {bucket_name} creado"}
    except Exception as e:
        return {"status": "error", "error": str(e)}
