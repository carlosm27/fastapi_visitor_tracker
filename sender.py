import pika
import json


tracker = {
        "ip_address": '127.0.0.1',
        "request_url": 'http://localhost:8000',
        "request_port": 8000,
        "request_path": "/",
        "request_method": "GET",
        "request_time": "2023-06-25T16:03:24.722256",
        "browser_type": "Firefox",
        "operating_system": "Windows 11",
    }

message =('127.0.0.1',
             'http://localhost:8000',
             8000,
             "/",
             "GET",
             "Edge",
             "Windows 11",
             "2023-06-25T16:03:24.722256"
             )

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='logs')

channel.basic_publish(exchange='', routing_key='logs', body=json.dumps(tracker))
print(" [x] Sent 'Logs'")
connection.close()