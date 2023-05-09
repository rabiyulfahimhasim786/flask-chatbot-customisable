from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chatbot', methods=['POST'])
def chatbot():
    message = request.form['message']
    response = {}

    if message.lower() == 'hi':
        response['message'] = 'Hi, are you looking for help?'
        response['options'] = ['Yes', 'No']

    elif message.lower() == 'yes':
        response['message'] = 'What kind of help are you looking for?'
        response['options'] = ['Help1', 'Help2', 'Help3']

    elif message.lower() == 'no':
        response['message'] = 'I am sorry, I didn\'t understand your request. Please fill out the form below:'
        response['form'] = True

    else:
        response['message'] = 'I am sorry, I didn\'t understand your request. Please try again.'
        response['options'] = ['Yes', 'No']

    return jsonify(response)
