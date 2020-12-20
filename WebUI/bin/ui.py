import flask
from database import select_all, get_routers, last_seen
from flask import Flask, render_template
import os
import sys

app = Flask(__name__)

@app.route("/all", methods=['get'])
def all():    
    table = select_all()
    return render_template("table.html", headings = table['Columns'], data=table['Rows'], title="All Network Entities")


@app.route("/routers", methods=['get'])
def routers():
    table = get_routers()
    return render_template("table.html", headings= table['Columns'], data=table['Rows'], title='Routers')

@app.route("/lastseen", methods=['get'])
def lastseen():    
    table = last_seen()
    return render_template("table.html", headings= table['Columns'], data=table['Rows'], title='Last Seen')



if (__name__ == '__main__'):        
    port = 8080
    if(len(sys.argv) > 1):
        port = sys.argv[1]
    app.run(port=port, host="0.0.0.0")
    