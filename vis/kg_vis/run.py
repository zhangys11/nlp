import os, sys, json, uuid
from flask import Flask, render_template, request
from graph import random_graph, random_connected_graph, graph_to_dict, d3_format, export_json
import uuid
import json
import pandas as pd
from flaskwebgui import FlaskUI

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024 # limit to 5MB

# routes
@app.route("/", methods=['GET', 'POST'])
def index():
    file = os.path.dirname(os.path.realpath(__file__)) + "/static/Associations_jiagu.json"            
    print(file)
    associations = json.load(open(file, 'r', encoding='utf-8'))
    return render_template("home.html", associations = associations)

@app.route("/about")
def about_page():
	return "Created by Dr. Zhang (oo@zju.edu.cn)"

@app.route("/submit", methods = ['GET', 'POST'])
def show_corpse():

    if request.method == 'POST':
        
        r = ''
        command_type = request.form["command_type"] # table or graph
        use_builtin = request.form["use_builtin"] # 'sentence_level'

        if use_builtin: # not None or empty
            file = os.path.dirname(os.path.realpath(__file__)) + "/" + use_builtin
            # print(file)
        else:
            # Read the File using Flask request
            file = request.files['dataFile']
            # save file in local directory
            file.save(file.filename)

        # Parse the data as a Pandas DataFrame type
        if file.lower().endswith('.csv'):
            data = pd.read_csv(file, delimiter='\t')
        else:
            data = pd.read_excel(file)

        if command_type == 'graph':
            pass
        else:
            # Return HTML snippet that will render the table
            r = data.to_html()

    # render_template("home.html", use_builtin = use_builtin, d = d, nobs = n, kg_result = r)
    return {'message': 'success', 'html': r}

import webbrowser
from threading import Timer

def open_browser():
    webbrowser.open_new('http://localhost:5020/')
      
if __name__ =='__main__':
    ## use netstat -ano|findstr 5020 to check port use
    # Timer(3, open_browser).start()
    # app.run(host="0.0.0.0", port=5020, debug = False)
    FlaskUI(app=app, server="flask", port=5020).run()
    