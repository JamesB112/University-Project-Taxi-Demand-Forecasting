import requests
import pyarrow.parquet as pq

URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_2022-01.parquet"
response = requests.get(URL)
pq.write_table(response.content, "../data/file_exp.parquet")