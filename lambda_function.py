import json
import boto3
import os
import time
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
from tools.config import aws_region, default_arn_topic, topicname, protocol, endpoint
from tools.sns import SnsSend


client = boto3.client('sns')

def lambda_handler(event, context):

    topicname = event['topicname']
    protocol = event['protocol']
    endpoint = event['endpoint']

    #INCLUDE CODE TO RUN FUNCTIONS OF CLASS SnsSend#
    #PUBLISH LAMBDA PACKAGE CODE WITH ALL DEPENDENCIES#
    #REFERENCE https://docs.aws.amazon.com/lambda/latest/dg/python-package.html #
    create_topic(topicname, protocol, endpoint)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Working!'),
        
     }
