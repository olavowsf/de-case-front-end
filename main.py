from fastapi import FastAPI
from pydantic import BaseModel
from google.cloud import pubsub_v1
import json

project_id = "playground-olavo-387508"
topic_id = "raw_message"
sub_id = "processed-msg-sub"

# Pub/Sub consumer timeout
timeout = 3.0

app = FastAPI()


class Item(BaseModel):
    time_stamp: str
    data: list


@app.post("/response/")
async def create_item(item: Item):
    item_dict = item.dict()
    data = json.dumps(item_dict)

    # Publish the data
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_id)
    message_id = publisher.publish(topic_path, data=data.encode("utf-8"))
    
    # Subscribe to the Pub/Sub topic and start receiving messages
        # Modify the data as needed and publish it
    def callback(message):
       return message
       message.ack()

    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(project_id, sub_id)
    streaming_pull_future = subscriber.subscribe(subscription_path,callback)
    with subscriber:
        try:                
            streaming_pull_future.result(timeout)
        except TimeoutError:
            streaming_pull_future.cancel()
    
    
    



