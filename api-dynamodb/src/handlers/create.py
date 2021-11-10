import json
import logging
import os
import time
import uuid

import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['catTableName'])


def create(event, context):
    data = json.loads(event['body'])
    if 'name' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the Cat item.")

    timestamp = str(time.time())

    item = {
        'id': str(uuid.uuid1()),
        'name': data['name'],
        'color': data.get('color', ''),
        'age': data.get('age', ''),
        'createdAt': timestamp,
        'updatedAt': timestamp,
    }

    table.put_item(Item=item)

    return {"statusCode": 200, "body": json.dumps(item)}
