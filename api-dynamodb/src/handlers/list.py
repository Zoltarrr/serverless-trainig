import json
import os

import boto3
from src.utils.decimal_encoder import DecimalEncoder

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['catTableName'])


def get(event, context):
    result = table.scan()
    return {
        "statusCode": 200,
        "body": json.dumps(result['Items'], cls=DecimalEncoder)
    }
