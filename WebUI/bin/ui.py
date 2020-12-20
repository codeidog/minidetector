import flask
from database import select_all, get_routers
from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/all", methods=['get'])
def all():    
    table = select_all()
    return render_template("table.html", headings = table['Columns'], data=table['Rows'])


@app.route("/routers", methods=['get'])
def routers():
    table = get_routers()
    return render_template("table.html", headings= table['Columns'], data=table['Rows'])

@app.route("/lastseen", methods=['get'])
def lastseen():    
    pass


if (__name__ == '__main__'):        
    port = os.environ['PORT']
    app.run(port=port, host="0.0.0.0")
    