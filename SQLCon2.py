import sqlalchemy as sa
import urllib
from sqlalchemy import create_engine, event

 
server = 'RIL-SPATHIRANNE' 
database = 'Emp' 
    #username = 'xxx' 
    #password = 'xxx' 
    
params = urllib.parse.quote_plus("DRIVER={SQL Server};"
                                     "SERVER="+server+";"
                                     "DATABASE="+database+";"
                                     )
    
engine = sa.create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))
    
qry = "select * from Emp.dbo.MTG1_DartSales_Unilever_20221218_Top100"
#qry = qry + "FROM [Sales].[Customer] C INNER JOIN [Sales].SalesTerritory t on t.TerritoryID = c.TerritoryID "
#qry = qry + "where StoreID is not null and PersonID is not null"

with engine.connect() as con:
    rs = con.execute(qry)
    for row in rs:
        print (row)

