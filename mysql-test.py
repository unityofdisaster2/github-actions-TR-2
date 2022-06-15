#!/usr/bin/python 
import mariadb 

conn = mariadb.connect(
    user="root",
    password="mipassword0",
    host="mariadb_service",
    database="demo")
cur = conn.cursor() 

some_name = "Georgi" 
cur.execute("SELECT CategoryID,CategoryName, Description FROM Categories") 

for CategoryID, CategoryName, Description in cur: 
    print(f"CategoryID: {CategoryID}, Last name: {Description}")
    
# #insert information 
# try: 
#     cur.execute("INSERT INTO employees (first_name,last_name) VALUES (?, ?)", ("Maria","DB")) 
# except mariadb.Error as e: 
#     print(f"Error: {e}")

# conn.commit() 
# print(f"Last Inserted ID: {cur.lastrowid}")
    
conn.close()