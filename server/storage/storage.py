import os
import paho.mqtt.client as mqtt
from uuid import uuid4
# import ibm_boto3
# from ibm_botocore.client import Config, ClientError
import boto3


endpoint = os.environ['COS_ENDPOINT']
bucket = os.environ['BUCKET']

cos = boto3.client('s3', endpoint_url=endpoint)

client = mqtt.Client('storage')
client.connect(os.environ['MQTT_BROKER'])


def on_message(client, userdata, message):
    cos.put_object(
        Body=message.payload,
        Bucket=bucket,
        Key='hw3/%s.jpg' % uuid4())


client.on_message = on_message

client.subscribe('jetson/webcam/faces')
client.loop_forever()
