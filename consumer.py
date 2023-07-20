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
                        tracker["browser_type"], tracker["operating_system"],tracker["request_time"])
    print(txt)

async def receiver(loop):
    connection = await aio_pika.connect("amqp://guest:guest@localhost/", loop = loop)
    channel =  await connection.channel()
    queue = await channel.declare_queue("logs")
        
       
    await queue.consume(on_message, no_ack=True)
    print(' [*] Waiting for messages.')
        
    
  
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(receiver(loop))
    loop.run_forever()

