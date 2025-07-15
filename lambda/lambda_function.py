import json
import boto3
import os
import time

s3 = boto3.client('s3')
BUCKET_NAME = os.environ.get('BUCKET_NAME')

def lambda_handler(event, context):
    key = f"file_{int(time.time())}.txt"
    s3.put_object(Bucket=BUCKET_NAME, Key=key, Body=b"Created by Lambda")
    return {
        'statusCode': 200,
        'body': json.dumps({'message': f'File {key} created'})
    }
