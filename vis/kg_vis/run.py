import os, sys, json, uuid
from flask import Flask, render_template, request
from graph import random_graph, random_connected_graph, graph_to_dict, d3_format, export_json
import uuid
import pandas as pd
from flaskwebgui import FlaskUI

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024 # limit to 5MB


def create_random_d3_graph_dict():
    """
    Creates a random NetworkX graph and returns a dictionary 
    representation of the graph formatted for visualization in d3
    """
    G = random_connected_graph(15)
    graph_dict = graph_to_dict(G)
    d3_graph_dict = d3_format(graph_dict)
    return d3_graph_dict


@app.route('/forcetree')
def get_force_tree():
    # create a random graph and export to static file
    d3_graph_dict = create_random_d3_graph_dict()
    export_json(d3_graph_dict)
    # client will load graph from static file
    return render_template("force-tree.html")


@app.route('/forcezoompan')
def get_force_zoom_pan():
    # create a random graph and export to static file
    d3_graph_dict = create_random_d3_graph_dict()
    export_json(d3_graph_dict)
    # client will load graph from static file
    return render_template("force-zoom-pan.html")


@app.route('/forcezoompan2')
def get_force_zoom_pan_2():
    # client will ask for graph data from /data route
    return render_template("force-zoom-pan-2.html")


@app.route('/data')
def get_data():
    # create a random graph and return json via flask
    d3_graph_dict = create_random_d3_graph_dict()
    return jsonify(dict(data=d3_graph_dict))

# routes
@app.route("/", methods=['GET', 'POST'])
def index():
	return render_template("home.html")

@app.route("/about")
def about_page():
	return "Created by Dr. Zhang (oo@zju.edu.cn)"

@app.get('/upload')
def upload():
    return render_template('upload_excel.html')

@app.post('/view')
def view():
 
    # Read the File using Flask request
    file = request.files['file']
    # save file in local directory
    file.save(file.filename)
 
    # Parse the data as a Pandas DataFrame type
    data = pd.read_excel(file)
 
    # Return HTML snippet that will render the table
    return data.to_html()

@app.route("/submit", methods = ['GET', 'POST'])
def show_corpse():
    if request.method == 'POST':
        
        r = ''
        use_builtin = request.form["use_builtin"] # 'sentence_level'

        if use_builtin: # not None or empty
            file = os.path.dirname(os.path.realpath(__file__)) + "/" + use_builtin
            print(file)
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

        # Return HTML snippet that will render the table
        r = data.to_html()

    # render_template("home.html", use_builtin = use_builtin, d = d, nobs = n, kg_result = r)
    return {'message': 'success', 'html': r}

'''
The Flask dev server is not designed to be particularly secure, stable, or efficient. 
By default it runs on localhost (127.0.0.1), change it to app.run(host="0.0.0.0") to run on all your machine's IP addresses.
0.0.0.0 is a special value that you can't use in the browser directly, you'll need to navigate to the actual IP address of the machine on the network. You may also need to adjust your firewall to allow external access to the port.
The Flask quickstart docs explain this in the "Externally Visible Server" section:
    If you run the server you will notice that the server is only accessible from your own computer, not from any other in the network. This is the default because in debugging mode a user of the application can execute arbitrary Python code on your computer.
    If you have the debugger disabled or trust the users on your network, you can make the server publicly available simply by adding --host=0.0.0.0 to the command line.
'''

import webbrowser
from threading import Timer

def open_browser():
    webbrowser.open_new('http://localhost:5020/')
      
if __name__ =='__main__':
    ## use netstat -ano|findstr 5005 to check port use
    # Timer(3, open_browser).start()
    # app.run(host="0.0.0.0", port=5005, debug = False)
    FlaskUI(app=app, server="flask", port=5020).run()
    