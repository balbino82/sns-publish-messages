import json
import boto3
import os
import time
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
from tools.config import aws_region, default_arn_topic

class SnsSend:
    def __init__(self, topicname, protocol, endpoint):
        self.topicname = topicname
        self.protocol = protocol
        self.endpoint = endpoint

    def create_topic(self, topicname):
        print('criando topico')
        client = boto3.client('sns')
        response_create_topic = client.create_topic(
            Name = topicname,
            Tags=[
                {
                    'Key': 'Test',
                    'Value': 'SNS'
                },
            ]
        )
        print('executei o response')
        topicarn = response_create_topic['TopicArn']
        print(topicarn)
        return topicarn
    
    def get_subscribers(self, topicname, protocol, endpoint):
        client = boto3.client('sns')
        topicarn = default_arn_topic+topicname
        protocol = protocol
        endpoint = endpoint

        response_subscribers = client.list_subscriptions_by_topic(
            TopicArn = topicarn
        )
        subscribers = (response_subscribers['Subscriptions'])

        if subscribers == []:
            response_subscriber = client.subscribe(
                TopicArn=topicarn,
                Protocol=protocol,
                Endpoint=endpoint
            )
            print('realizando subscricao')
            return response_subscriber
        else:
            print('sem necessidade de subscricao')
            return True
    
    def publish_message_fail (self, topicname, protocol, endpoint):
        client = boto3.client('sns')
        topicarn = default_arn_topic+topicname
        message = {"Validate": "wasabi validate template fail"}
        response_publish = client.publish(
            TopicArn = topicarn,
            Message = json.dumps({'default': json.dumps(message)}),
            Subject = 'Pipeline Validate Fail',
            MessageStructure = 'json'
        )
        print('publicando mensagem de falha')

    def publish_message_success (self, topicname, protocol, endpoint):
        client = boto3.client('sns')
        topicarn = default_arn_topic+topicname
        message = {"Validate": "wasabi validate template success"}
        response_publish = client.publish(
            TopicArn = topicarn,
            Message = json.dumps({'default': json.dumps(message)}),
            Subject = 'Pipeline Validate Success',
            MessageStructure = 'json'
        )
        print('publicando mensagem de sucesso')
