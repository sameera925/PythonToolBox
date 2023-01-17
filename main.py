import os
import pandas as pd
import sqlalchemy

server = "."
database = "Emp"

ODBC_DIVER = "ODBC Driver 17 for SQL Server"
DRIVER = ODBC_DIVER.replace(" ", "+")
host = rf"{server}/{database}?trusted_connection=yes&driver={DRIVER}"
conn_str = f"mssql://{server}/{database}?@{host}"
engine = sqlalchemy.create_engine(conn_str)

qry = "SELECT * FROM Emp.dbo.MTG_text_READY"   # query to get data for extract
extract_location = "C:\mapping\CSV" # location to save extract
file_name = "MTG1_DartSales_Unilever_20221212.parquet" # name of extract

qry_results: pd.DataFrame = pd.read_sql_query(
    qry, engine
)
print(qry_results)

landing_location = os.path.join(extract_location, file_name)

qry_results.to_parquet(landing_location, index=False)
print(f"[info] {file_name} generated to {landing_location}")
