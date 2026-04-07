import redis
import json
import time
import random

redis_client = redis.Redis(host='redis', port=6379, decode_responses=True)
channel = "orders"
order_id = 1

while True:
    order = {
        "event": "OrderCreated",
        "order_id": order_id,
        "user": f"user{random.randint(1,5)}",
        "amount": random.randint(100, 1000)
    }
    message = json.dumps(order)
    redis_client.publish(channel, message)
    print(f"[ORDER SERVICE] Order created: {message}")
    order_id += 1

    time.sleep(5)
