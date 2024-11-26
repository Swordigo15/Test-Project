import pyodbc

SERVER = 'LAPTOP-DT3VAS88'
DATABASE = 'MONDIAL'
USERNAME = 'root'
PASSWORD = ''

connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

conn = pyodbc.connect(connectionString)

SQL_QUERY = """
    SELECT o.Name, c.Name, im.Type 
    FROM isMember im 
    JOIN organization o ON im.Organization = o.Abbreviation 
	JOIN country c ON c.Code = im.Country
    WHERE im.Country = 1;
"""

cursor = conn.cursor()
cursor.execute(SQL_QUERY)