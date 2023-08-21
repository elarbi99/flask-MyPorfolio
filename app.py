from flask import Flask, render_template,request
from flask_cors import CORS
from models import create_data, get_data
from flask_mail import Mail, Message
import smtplib
import os
app = Flask(__name__,template_folder='templates',static_folder='static')
CORS(app)
app.config['TESTING'] = False
@app.route('/',methods=['GET'])
def index():
    testimonial=get_data()
    return render_template('index.html',testimonial=testimonial)

@app.route('/contact',methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')  
        phone = request.form.get('phone')  
        comment = request.form.get('comment')
        
        # Create and send the email
        subject = 'New Contact'
        body = f'Name: {name}\nEmail: {email}\nPhone: {phone}\nComment: {comment}'
        
        try:
            conn = smtplib.SMTP('smtp.gmail.com', 587)
            conn.ehlo()
            conn.starttls()
            conn.set_debuglevel(1)
            conn.login('t30710948@gmail.com', 'aoozlhvtwfbemyqt')

            send = 'elarbi_m@protonmail.com'
            conn.sendmail('t30710948@gmail.com', send, f'Subject: {subject}\n\n{body}')
        except smtplib.SMTPException as e:
            error_message = f'An error occurred: {e}'
            return render_template('contact.html', error=error_message)

    return render_template('contact.html',success=False)

@app.route('/testimonial', methods=['GET', 'POST'])
def testimonial():
    success = False  # Default status is not successful
    if request.method == 'POST':
        name = request.form.get('name')
        comment = request.form.get('comment')
        try:
            create_data(name, comment)
            success = True  # Update status if data is successfully submitted
        except Exception as e:
            print("Error:", e)
    return render_template('testimonial.html', success=success)

if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)