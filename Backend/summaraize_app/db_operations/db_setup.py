import mysql.connector

def setup_db():
  # Using mysql-connector-python
  mydb = mysql.connector.connect(
  host="localhost",       # or your host, e.g., "127.0.0.1"
  user="root",    # your database username
  password="Sachin@01",# your database password
  database="summaraize"   # the name of the database you want to connect to
  )
  return mydb

