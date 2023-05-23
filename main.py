from fastapi import FastAPI, Body, Form, Depends
from src.database import transform,insert_row
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    time_stamp: str
    data: list



@app.post("/response/")
async def create_item(item: Item):

    item_dict = item.dict()
    response = transform(item_dict)
    job = insert_row(response)

    if job == None:
        result = f"The following row: {response} has been added."
    else:
        result = "Encountered errors while inserting rows: {}".format(job)

    return result
