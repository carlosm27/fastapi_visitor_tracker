

from fastapi import FastAPI


from controllers import all_logs, new_log
import json    
import asyncio
import aio_pika
from consumer import on_message

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]
methods = ["GET", "POST", "PUT", "DELETE"]
headers = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=methods,
    allow_headers=headers,
)

@app.on_event('startup')
async def startup():
    loop = asyncio.get_event_loop()
    connection = await aio_pika.connect("amqp://guest:guest@localhost/", loop = loop)
    channel =  await connection.channel()
    queue = await channel.declare_queue("logs")
    await queue.consume(on_message, no_ack=True)




@app.get("/logs")
async def receiver():
    logs = all_logs()
    return logs
    



@app.get("/")
async def hello():
    
    return "hello"




