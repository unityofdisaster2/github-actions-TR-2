#!/usr/bin/python 
import mariadb 

conn = mariadb.connect(
    user="root",
    password="mipassword0",
    host="mariadb_service",
    database="nation")

try: 
	cur = conn.cursor() 

	cur.execute("SELECT name, area FROM countries LIMIT 10") 

	for name, area in cur: 
		print(f"name: {name}, area: {area}")
except Exception:
	print('something went wrong')
	print(Exception)

conn.close()