from flask import Flask, render_template, request, redirect, url_for
from joblib import load
import pandas as pd
import numpy as np
#from get_tweets import get_related_tweets


pipeline = load("text_classification.joblib")


def requestResults(name):
    # tweets = get_related_tweets(name)
    tweets = pd.read_csv("text.csv")
    tweets = pipeline.predict(tweets['new_tweets'])
    # data = str(tweets.value_counts()) + '\n\n'
    data = str(np.unique(tweets, return_counts=True)) + '\n\n'

    output = data + str(tweets)
    return output


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        user = request.form['search']
        return redirect(url_for('success', name=user))


@app.route('/success/<name>')
def success(name):
    return "<xmp>" + str(requestResults(name)) + " </xmp> "


if __name__ == '__main__' :
    app.run(debug=True)