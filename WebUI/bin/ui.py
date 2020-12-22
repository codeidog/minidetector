import flask
from database import Entity, create_session
from flask import Flask, render_template
from sqlalchemy import func, desc
from sqlalchemy.orm import Query
import os
import sys
import logging

app = Flask(__name__)
error_message = "An error occurred"
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.DEBUG    
    )
@app.route("/all", methods=['get'])
def all():    
    print('Getting all the devices')
    query = Query(Entity).with_entities(Entity.mac, Entity.ip)
    return get_result_template(query)
        


@app.route("/routers", methods=['get'])
def routers():
    print('Getting all the routers')
    query = Query(Entity).group_by(Entity.mac).\
            having(func.count(Entity.mac) > 3).\
            with_entities(Entity.mac)
    return get_result_template(query)

@app.route("/lastseen", methods=['get'])
def lastseen():    
    print('Getting the last seen devices')    
    query = Query(Entity).order_by(desc(Entity.last_seen)).\
            with_entities(Entity.mac, Entity.ip, Entity.last_seen)
    return get_result_template(query)

def get_result_template(query: Query):
    result = execute_query(query)
    if(type(result) is Query):
        data = result.all() 
        columns = [col['name'] for col in query.column_descriptions]
        return render_template("table.html", headings= columns, data=data, title='Last Seen')        
    else:
        return query


def execute_query(query: Query):
    result = error_message
    session = create_session()
    try:
        print(f'Query to run: {query}')                        
        result = query.with_session(session)        
    except Exception as e:
        print(f'{result}: {e}')
    finally:
        session.close()
        return result

if (__name__ == '__main__'):        
    port = 8081
    if(len(sys.argv) > 1 and type(sys.argv[1]) is int):
        port = sys.argv[1]    
    app.run(port=port, host="0.0.0.0")
    