from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import Column, Integer, String

# app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chatbot.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(50), nullable=False)
    version = db.Column(db.String(50), nullable=False)
    mobile = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)
if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
    create_database(app.config['SQLALCHEMY_DATABASE_URI'])
    app.app_context().push()
    db.create_all()
    db.session.commit()

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/api/chatbot', methods=['POST'])
# def chatbot():
#     message = request.form['message']
#     response = {}

#     if message.lower() == 'hi':
#         response['message'] = 'Hi, are you looking for help?'
#         response['options'] = ['Yes', 'No']

#     elif message.lower() == 'yes':
#         response['message'] = 'What kind of help are you looking for?'
#         response['options'] = ['Help1', 'Help2', 'Help3']

#     # elif message.lower() == 'no':
#     #     response['message'] = 'I am sorry, I didn\'t understand your request. Please fill out the form below:'
#     #     response['form'] = True
#     elif message.lower() == 'no':
#         response['message'] = 'I am sorry, I didn\'t understand your request. Please fill out the form below:'
#         response['form'] = True
#         # Save the data to the database
#         name = request.form['name']
#         email = request.form['email']
#         mobile = request.form['mobile']
#         user = User(name=name, email=email, mobile=mobile)
#         db.session.add(user)
#         db.session.commit()


#     else:
#         response['message'] = 'I am sorry, I didn\'t understand your request. Please try again.'
#         response['options'] = ['Yes', 'No']

#     return jsonify(response)
@app.route('/api/chatbot', methods=['POST', 'GET'])
def chatbot():
    message = request.form['message']
    response = {}

    if message.lower() == 'magento':
        response['message'] = 'do you need to build new site'
        response['options'] = ['Yes', 'No']

    elif message.lower() == 'yes':
        response['message'] = 'What is your website url and your current version for magento?'
        # response['options'] = ['Help1', 'Help2', 'Help3']
        response['form'] = True

    elif message.lower() == 'no':
        response['message'] = 'Do you need to redesign or Do you need to any maintenance and support? select below:'
        # response['form'] = True
        response['options'] = ['redesign', 'maintenance and support']

        #Save the data to the database
        # name = request.form.get('name')
        # email = request.form.get('email')
        # mobile = request.form.get('mobile')
        # name = request.form['name']
        # email = request.form['email']
        # mobile = request.form['mobile']
        # if request.method == 'POST':
        # if message == 'form':
        #     return {
        #     'message': 'Please fill out the form',
        #     }
            #message = request.form.get('message')
        # name = request.form.get('name')
        # email = request.form.get('email')
        # mobile = request.form.get('mobile')
        #     # name = request.form['name']
        #     # email = request.form['email']
        #     # mobile = request.form['mobile']
        

        # print(name, email, mobile)
        # if name and email and mobile:
        #     user = User(name=name, email=email, mobile=mobile)
        #     db.session.add(user)
        #     db.session.commit()
        #     response['message'] = 'Thanks for submitting the form!'
        #     #response['form'] = False
        # else:
        #     response['message'] = 'Please fill out all fields.'
    elif message.lower() == 'redesign':
        response['message'] = 'What is your website url and your current version for magento?'
        response['form'] = True
    elif message.lower() == 'maintenance and support':
        response['message'] = 'What is your website url and your current version for magento?'
        response['form'] = True
    else:
        response['message'] = 'I am sorry, I didn\'t understand your request. Please try again.'
        response['options'] = ['Yes', 'No']

    return jsonify(response)


@app.route('/submit-form', methods=['POST'])
def submit_form():
    url = request.form.get('url')
    version = request.form.get('version')
    mobile = request.form.get('mobile')
    email = request.form.get('email')
    # do something with the form data
    print(url, version, email, mobile)
    if url and version and email and mobile:
        user = User(url=url, version=version, email=email, mobile=mobile)
        db.session.add(user)
        db.session.commit()
        #response['message'] = 'Thanks for submitting the form!'
        return jsonify({'message': 'Form submitted successfully!'})
            #response['form'] = False
    else:
        #response['message'] = 'Please fill out all fields.'
        return jsonify({'message': 'Form submitted successfully!'})
    return jsonify({'message': 'Form submitted successfully!'})
