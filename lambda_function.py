import json
import boto3
from datetime import datetime

s3 = boto3.client('s3')

def lambda_handler(event, context):
    timestamp = datetime.now().isoformat()
    s3.put_object(
        Bucket='event-pipeline-bucket-2c5bf141',
        Key=f"events/{timestamp}.json",
        Body=json.dumps(event)
    )
    return {
        'statusCode': 200,
        'body': 'Event saved to S3'
    }
