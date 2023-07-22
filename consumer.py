import pika
import os, sys
from controllers import new_log
import json    
import asyncio
import aio_pika  
import ast

async def on_message(message: aio_pika.IncomingMessage):
    tracker = ast.literal_eval(message.body.decode("utf-8"))
    print(type(tracker))
    #tracker = json.loads(txt)
    print(type(tracker))
    new_log(tracker["ip_address"], tracker["request_url"], tracker["request_port"],
                        tracker["request_path"], tracker["request_method"],
                        tracker["browser_type"],tracker["request_time"], tracker["service_name"])
    print(tracker)



