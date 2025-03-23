from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mail import Mail, Message
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get("EMAIL_USER")  # Set your email
app.config['MAIL_PASSWORD'] = os.environ.get("EMAIL_PASS")  # Set your app password

mail = Mail(app)

@app.route('/', methods=['GET'])
def home():
    return app.send_static_file('EmailSending.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON data"}), 400

        sender = data.get('sender')
        recipient = data.get('recipient')
        subject = data.get('subject')
        message = data.get('message')

        if not all([sender, recipient, subject, message]):
            return jsonify({"error": "All fields are required"}), 400

        msg = Message(subject, sender=sender, recipients=[recipient])
        msg.body = message
        mail.send(msg)

        return jsonify({'message': 'Email sent successfully!'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5001, debug=True)
