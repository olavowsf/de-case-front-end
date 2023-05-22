from fastapi import FastAPI
from database import transform, insert_row

app = FastAPI()


@app.post("/response")
async def create_item(item: dict):
    raw_response = item
    response = transform(raw_response)
    job = insert_row(response)

    if job == None:
        result = f"The following row: {response} has been added."
    else:
        result = "Encountered errors while inserting rows: {}".format(job)

    return result 

