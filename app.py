from flask import Flask, render_template,request

app = Flask(__name__,template_folder='templates',static_folder='static')


@app.route('/')
def hello():
    return render_template('index.html')


if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True, port=33507)