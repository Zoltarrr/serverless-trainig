import csv
import io
import json
import os
import urllib.parse
import boto3


s3 = boto3.client('s3')
sqs_client = boto3.client('sqs', region_name=os.environ['REGION'])


def lambda_handler(event, context):
    print(event)
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

    try:
        file = s3.get_object(Bucket=bucket_name, Key=key)
        file_data = file['Body'].read().decode('utf-8')
        spam_reader = csv.reader(io.StringIO(file_data), delimiter=' ', quotechar='|')

        cat_data = []
        for line in list(spam_reader)[1:]:
            n, c, a = line[0].split(',')
            cat_data.append({'name': n, 'color': c, 'age': a})

        response = sqs_client.send_message(
            QueueUrl=os.environ['QUEUE_URL'],
            MessageBody=json.dumps(cat_data)
        )
        print(cat_data)
        print('RESPONSE', response)

    except Exception as e:
        print(e)
