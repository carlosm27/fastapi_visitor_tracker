from robyn import Robyn, status_codes

from fastapi import FastAPI
from robyn.robyn import Response

from controllers import all_logs, new_log
import json    
import asyncio
import aio_pika
from consumer import on_message

app = FastAPI()

@app.on_event('startup')
async def startup():
    loop = asyncio.get_event_loop()
    connection = await aio_pika.connect("amqp://guest:guest@localhost/", loop = loop)
    channel =  await connection.channel()
    queue = await channel.declare_queue("logs")
    await queue.consume(on_message)




@app.get("/message")
async def receiver():
    logs = all_logs()
    return logs
    



@app.get("/")
async def hello():
    
    return "hello"




