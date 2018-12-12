from flask import Flask, render_template
from pull_data import returnDF

app = Flask(__name__)

@app.route('/index')
def hello_world():

    data = returnDF().to_html()

    return render_template('index.html', data=data)