from robyn import Robyn, status_codes

from fastapi import FastAPI
from robyn.robyn import Response

from controllers import all_logs, new_log
import json    
import asyncio
import aio_pika  

app = FastAPI()

@app.on_event('startup')
async def startup():
    loop = asyncio.get_event_loop()
    conn = await aio_pika.connect_robust('amqp://guest:guest@localhost:5672', loop=loop)
    channel = await conn.channel()
    queue = await channel.declare_queue('logs')

    
    def consumer(message: aio_pika.Message):
        print(message.body)
        txt = message.body.decode("utf-8")
        tracker = json.loads(txt)
        new_log(tracker["ip_address"], tracker["request_url"], tracker["request_port"],
                        tracker["request_path"], tracker["request_method"],
                        tracker["browser_type"], tracker["operating_system"],tracker["request_time"])

    await queue.consume(consumer)


@app.get("/message")
async def receiver():
    logs = all_logs()
    return logs
    



@app.get("/")
async def hello():
    
    return "hello"




