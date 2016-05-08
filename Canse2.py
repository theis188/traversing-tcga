import os
import re
import numpy
import time
from scipy import stats
import matplotlib.pyplot as plt
import sklearn
from Canse1fun import getData 
from Canse1fun import listChange
import psycopg2

DatArray = getData()
DatArray = DatArray[0][0:2]
#print DatArray
#a = raw_input('Blah...')

<<<<<<< HEAD
#conn = psycopg2.connect("host=localhost dbname=postgres user=postgres port=5433 password=")
#cur = conn.cursor()
#cur.execute("select relname from pg_class where relkind = 'r' and relname !~ '^(pg_|sql_)' ;")
#print cur.fetchall()
=======
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres port=5432 password=")
cur = conn.cursor()
cur.execute("select relname from pg_class where relkind = 'r' and relname !~ '^(pg_|sql_)' ;")
print cur.fetchall()
>>>>>>> 44b633a8fe130871da75ce82f1b59222cfcda17a

#cur.execute("DROP TABLE cancer_data")

#cur.execute("""CREATE TABLE IF NOT EXISTS cancer_data(
#patient_id text,
#gender text
#);""")

#for i in range(len(DatArray[0])):
#	query = "INSERT INTO cancer_data (patient_id, gender) VALUES (%s, %s);"
#	data = (DatArray[0][i], DatArray[1][i])
#	cur.execute(query,data)

#cur.execute("select relname from pg_class where relkind = 'r' and relname !~ '^(pg_|sql_)' ;")
#print cur.fetchall()
#cur.execute("SELECT * FROM cancer_data;")
#print cur.fetchall()

conn.commit()
cur.close()
conn.close()
