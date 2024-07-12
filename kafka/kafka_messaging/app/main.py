 
from aiokafka import AIOKafkaProducer
from app.settings import BOOTSTRAP_SERVER,KAFKA_ORDER_TOPIC
from fastapi import FastAPI
import json
app = FastAPI()
@app.get("/")
def read_root():
    return {"App": " nalix xe s new inventory_service"}
@app.post("/create_order")
async def create_order(order:str):
    producer = AIOKafkaProducer(bootstrap_servers="broker:19092")
    await producer.start()
    order_json = json.dumps(order).encode('utf8')
    try:
        await producer.send_and_wait("topic",order_json)
    finally:
        await producer.stop()
    return order_json  