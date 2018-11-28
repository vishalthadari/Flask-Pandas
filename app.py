import flask
from flask import Flask, request, render_template
from flask import url_for, flash, redirect
import pandas as pd
import model

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return flask.render_template('index.html')


@app.route('/task1', methods=['GET', 'POST'])
def filterData():
    if request.method == 'POST':

        file = request.files['excel']
        if not file:
            flash('No file part')

        data = pd.read_excel(file)
        validate = False
        validate = model.childDataset(data)

        return flask.render_template('index.html', validate=validate)


@app.route('/task2', methods=['GET', 'POST'])
def roundOff():
    if request.method == 'POST':

        file = request.files['excel']
        if not file:
            flash('No file part')

        data = pd.read_excel(file)
        validate1 = False
        validate1 = model.retentionTime(data)

        return flask.render_template('index.html', validate1=validate1)


@app.route('/task3', methods=['GET', 'POST'])
def roundOffMean():
    if request.method == 'POST':

        file = request.files['excel']
        if not file:
            flash('No file part')

        data = pd.read_excel(file)
        validate2 = False
        validate2 = model.mean(data)

        return flask.render_template('index.html', validate2=validate2)



if __name__ == '__main__':

    # start api
    app.secret_key = "secret-key"
    app.run(host='0.0.0.0', port=8000, debug=True)
