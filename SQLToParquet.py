#import pandas as pd
import pypyodbc as odbc 

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'RIL-SPATHIRANNE'
DATABASE_NAME = 'Emp'

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}}; 
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
"""

conn = odbc.connect(connection_string)
print(conn)


#import pyodbc
#conn = pyodbc.connect('Driver={SQL Server};'
#                      'Server=RON\SQLEXPRESS;'
#                      'Database=test_database;'
#                      'Trusted_Connection=yes;')
#import sqlalchemy
#import pyarrow as pa
#import pyarrow.parquet as pq
#import os, shutil
#import os.path
#from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
#from azure.keyvault.secrets import SecretClient
#from azure.identity import DefaultAzureCredential
#import requests
#import json
#from datetime import timedelta, date


