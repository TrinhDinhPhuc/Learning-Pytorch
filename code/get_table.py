from google.cloud import bigquery
import os
import pandas as pd
import numpy as np
#TODO: INITIALIZING BIGQUERY CONFIGURATION
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= "D:\Codes\pops-dab1c699446f.json"
client = bigquery.Client()
#TODO: PERFORM A QUERY
QUERY = ('SELECT * FROM `pops-204909.2017.YouTube_popsww_M_2017`')
query_job = client.query(QUERY)  # API request
rows = query_job.result()  # Waits for query to finish
#TODO: READ EXCEL FILE
metadata = pd.read_excel("Kids.xlsx")
data = pd.DataFrame(columns=['date','video_id','content_type','average_view_duration_seconds','channel_id','asset_id','asset_labels','views','estimated_partner_revenue'])
#TODO: Initializers
n_row = 100000
for i_row,row in enumerate(rows):
    data.loc[i_row] = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]]
    if i_row != 0 and i_row % 5000 == 0:
        print round((float(int(i_row) / float(n_row)) * 100), 2), "%"
    if i_row == n_row:
        data.to_excel("Kids.xlsx")
        print ("Done!")
        break