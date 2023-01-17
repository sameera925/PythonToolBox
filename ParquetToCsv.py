import pandas as pd

parquet_location = "C:/mapping/CSV/MTG1_DartSales_Unilever_20221212.parquet"
csv_location = "C:/mapping/CSV/SampleExtract.csv"

df = pd.read_parquet(parquet_location)
df.to_csv(csv_location,index=False)
