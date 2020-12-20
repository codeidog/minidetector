import psycopg2
import logging
import os
db_server = os.environ['DB_SERVER']
db_name = os.environ['DB_NAME']
db_user = os.environ['DB_USER']
db_pwd = os.environ['DB_PWD']
constr = f'dbname={db_name} user={db_user} host={db_server} password={db_pwd}'


def select_all():
    query = "SELECT mac, ip FROM entity"    
    with psycopg2.connect(constr) as conn:
      cursor = conn.cursor()      
      cursor.execute(query)
      colnames = [desc[0] for desc in cursor.description]
      rows = cursor.fetchall()      
    return {
      "Columns" : colnames,
      "Rows": rows
    }

def get_routers():
    query = "SELECT mac FROM entity GROUP BY mac HAVING COUNT(mac) >3"    
    with psycopg2.connect(constr) as conn:
      cursor = conn.cursor()      
      cursor.execute(query)
      colnames = [desc[0] for desc in cursor.description]
      rows = cursor.fetchall()      
    return {
      "Columns" : colnames,
      "Rows": rows
    }

def last_seen():
  query = "SELECT mac, ip, last_seen FROM entity ORDER BY last_seen DESC"    
  with psycopg2.connect(constr) as conn:
    cursor = conn.cursor()      
    cursor.execute(query)
    colnames = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()      
  return {
    "Columns" : colnames,
    "Rows": rows
  }
