import pandas as pd
import mysql.connector 
import json

with open("credentials.json", 'r') as fr:
    credentials = json.load(fr)

mydb = mysql.connector.connect(
    host="localhost", # IP address
    port="3306", # 3317
    user=credentials['user'],
    password=credentials['pass']
)

cursor = mydb.cursor()
cursor.execute('USE sakila')
df = pd.read_sql('SELECT * FROM actor', con=mydb)

print (df)