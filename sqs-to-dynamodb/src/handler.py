import json
import os
import time
import uuid

import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['catTableName'])


def lambda_handler(event, context):
    with table.batch_writer() as batch:
        for record in event['Records']:
            for item in json.loads(record['body']):
                timestamp = str(time.time())
                content = {
                    'id': str(uuid.uuid1()),
                    'name': item['name'],
                    'color': item.get('color', ''),
                    'age': item.get('age', ''),
                    'createdAt': timestamp,
                    'updatedAt': timestamp,
                }
                batch.put_item(Item=content)
