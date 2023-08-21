from flask import Flask, render_template,request
from flask_cors import CORS
from models import create_data, get_data
import os
app = Flask(__name__,template_folder='templates',static_folder='static')
CORS(app)

@app.route('/',methods=['GET'])
def index():
    testimonial=get_data()
    return render_template('index.html',testimonial=testimonial)

@app.route('/testimonial', methods=['GET', 'POST'])
def testimonial():
    if request.method=="POST":
        name =request.form.get('name')
        comment = request.form.get('comment')
        create_data(name,comment)
    return render_template('testimonial.html')

if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)