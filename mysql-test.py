#!/usr/bin/python 
import mariadb 

conn = mariadb.connect(
    user="root",
    password="mipassword0",
    host="mariadb_service",
    database="nation")
cur = conn.cursor() 

cur.execute("SELECT name, area, national_day FROM countries") 

for name, area, national_day in cur: 
    print(f"name: {name}, area: {area}, national day: {national_day}")
    
# #insert information 
# try: 
#     cur.execute("INSERT INTO employees (first_name,last_name) VALUES (?, ?)", ("Maria","DB")) 
# except mariadb.Error as e: 
#     print(f"Error: {e}")

# conn.commit() 
# print(f"Last Inserted ID: {cur.lastrowid}")
    
conn.close()