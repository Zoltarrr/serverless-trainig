import json
import os

import boto3

from src.utils.decimal_encoder import DecimalEncoder

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['catTableName'])


def get(event, context):
    cat_id = event['pathParameters']['id']
    result = table.get_item(Key={'id': cat_id})

    return {
        "statusCode": 200,
        "body": json.dumps(result['Item'], cls=DecimalEncoder)
    }
