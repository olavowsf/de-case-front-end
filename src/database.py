from google.cloud import bigquery
from datetime import datetime
from statistics import mean, stdev
from pytz import timezone

def create_table():

    client = bigquery.Client()

    dataset_id = "{}.my_dataset".format(client.project)

    dataset = bigquery.Dataset(dataset_id)
    dataset.location = "US"
    dataset = client.create_dataset(dataset, timeout=30) 

    table_id = f"{client.project}.my_dataset.my_table_name"

    table_schema = {
              'name': 'time_stamp',
              'type': 'STRING',
              'mode': 'REQUIRED'
              }, {
              'name': 'data',
              'type': 'STRING',
              'mode': 'REQUIRED'
              }

    table = bigquery.Table(table_id, schema=table_schema)
    table = client.create_table(table)  

def transform(response: dict):


    dt = datetime.fromisoformat(response['time_stamp'])
    utc_dt = dt.astimezone(timezone('UTC'))

    response['time_stamp'] = str(utc_dt)
    response['data'] = [ mean(response['data']), stdev(response['data'])]

    response["data"] = str(response["data"])
    data = []
    data.append(response)
    return data


def insert_row(response: list):

    client = bigquery.Client()
    dataset_id = "{}.my_dataset".format(client.project)
    dataset = bigquery.Dataset(dataset_id)
    table_id = f"{client.project}.my_dataset.my_table_name"

    destination = dataset.table("my_table_name")

    errors = client.insert_rows_json(table_id, response) 



