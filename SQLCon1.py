import pandas as pd
import pyodbc
import sqlalchemy as sa

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=RIL-SPATHIRANNE;'
                      'Database=Emp;'
                      'Trusted_Connection=yes;')

sql_query = pd.read_sql_query(''' 
                              SELECT * FROM Emp.dbo.MTG1_DartSales_Unilever_20221218
                              '''
                              ,conn) # here, the 'conn' is the variable that contains your database connection information from step 2

df = pd.DataFrame(sql_query)
df.to_csv (r'C:\mapping\CSV\exported_data.csv', index = False) # place 'r' before the path name