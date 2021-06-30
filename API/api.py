import flask
import json
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

with open('../Databases/DMC/dmc.json') as file:
    database_dmc = json.load(file)


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Floss Database</h1>'''


@app.route('/api/v1/resources/dmc/all', methods=['GET'])
def api_all():
    return jsonify(database_dmc)


@app.route('/api/v1/resources/dmc', methods=['GET'])
def api_name():
    if 'name' in request.args:
        name = request.args['name']
        results = []
        for floss in database_dmc:
            if floss['name'] == name:
                results.append(floss)
        return jsonify(results)
    else:
        return "Error: No name field provided. Please specify an name."


app.run()
