from fastapi import FastAPI
from src.database import transform, insert_row, create_dataset, create_table
from pydantic import BaseModel
from google.cloud import pubsub_v1
import json

project_id = "playground-olavo-387508"
topic_id = "raw_message"

app = FastAPI()


class Item(BaseModel):
    time_stamp: str
    data: list


@app.post("/response/")
async def create_item(item: Item):
    item_dict = item.dict()
    data = json.dumps(item_dict)

    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_id)
    message_id = publisher.publish(topic_path, data=data.encode("utf-8"))
    return f"Published message: {message_id}"


























#    response = transform(item_dict)
#    job_result = insert_row("my_dataset", "my_table", response)
#
#    if job_result == []:
#        result = f"The following row: {response} has been added."
#    else:
#        result = job_result
#
#    return result
