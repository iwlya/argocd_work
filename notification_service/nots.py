import redis
import json

redis_client = redis.Redis(host='redis', port=6379, decode_responses=True)

pubsub = redis_client.pubsub()

channel = "orders"

pubsub.subscribe(channel)

for message in pubsub.listen():

    if message["type"] == "message":
        data = json.loads(message["data"])
        if data["event"] == "OrderCreated":
            print(
                f"[NOTIFICATION] Send notification: "
                f"Order {data['order_id']} created for {data['user']} "
                f"amount {data['amount']}"
            )
