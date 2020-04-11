import json, boto3, os, time, logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
from tools.config import aws_region, default_arn_topic, topicname, protocol, endpoint
from tools.sns import SnsSend
topicname = topicname
protocol = protocol
endpoint = endpoint
sns = SnsSend(topicname, protocol, endpoint)
sns.create_topic(topicname)
sns.get_subscribers(topicname, protocol, endpoint)
time.sleep(2)
sns.publish_message_fail(topicname, protocol, endpoint)
time.sleep(2)
sns.publish_message_success(topicname, protocol, endpoint)
time.sleep(2)
