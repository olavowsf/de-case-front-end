from google.cloud import bigquery
from datetime import datetime
from statistics import mean, stdev
from pytz import timezone




def create_dataset(dataset_name: str):
    client = bigquery.Client()
    dataset_id = "{}.{}".format(client.project,dataset_name)
    
    dataset = bigquery.Dataset(dataset_id)
    dataset.location = "US"
    dataset = client.create_dataset(dataset, timeout=30)
    
    return dataset_id

def create_table(dataset_name: str, table_name: str):
    client = bigquery.Client()

    dataset_id = create_dataset(dataset_name)

    table_id = f"{dataset_id}.{table_name}"

    table_schema = {"name": "time_stamp", "type": "STRING", "mode": "REQUIRED"}, {
        "name": "data",
        "type": "STRING",
        "mode": "REQUIRED",
    }

    table = bigquery.Table(table_id, schema=table_schema)
    table = client.create_table(table)

    return dataset_id, table_id


def transform(response: dict):
    dt = datetime.fromisoformat(response["time_stamp"])
    utc_dt = dt.astimezone(timezone("UTC"))

    response["time_stamp"] = str(utc_dt)
    response["data"] = [mean(response["data"]), stdev(response["data"])]

    response["data"] = str(response["data"])
    data = []
    data.append(response)
    return data


def insert_row(dataset_name: str, table_name: str, response: list):
    client = bigquery.Client()
    
    table_id = f"{client.project}.{dataset_name}.{table_name}"

    errors = client.insert_rows_json(table_id, response)
    return errors