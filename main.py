from fastapi import FastAPI
from src.database import transform,insert_row, create_dataset, create_table
from pydantic import BaseModel




dataset_id, table_id = create_table("my_dataset", "my_table")

app = FastAPI()
class Item(BaseModel):
    time_stamp: str
    data: list

@app.post("/response/")
async def create_item(item: Item):

    item_dict = item.dict()
    response = transform(item_dict)
    job_result = insert_row("my_dataset", "my_table", response)

    if job_result == []:
        result = f"The following row: {response} has been added."
    else:
        result = job_result

    return result
