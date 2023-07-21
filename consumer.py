import pika
import os, sys
from controllers import new_log
import json    
import asyncio
import aio_pika  

async def on_message(message: aio_pika.IncomingMessage):
    txt = message.body.decode("utf-8")
    tracker = json.loads(txt)
    new_log(tracker["ip_address"], tracker["request_url"], tracker["request_port"],
                        tracker["request_path"], tracker["request_method"],
                        tracker["browser_type"], tracker["operating_system"],tracker["request_time"], tracker["service_name"])
    print(txt)



