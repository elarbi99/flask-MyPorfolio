from flask import Flask, render_template,request

app = Flask(__name__,template_folder='templates',static_folder='static')


@app.route('/')
def hello():
    return render_template('index.html')
