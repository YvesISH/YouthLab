# from email.message import EmailMessage
# import os
# import smtplib
from flask import Flask, render_template
# from requests import request

app = Flask(__name__)

# def get_image_files():
#     img_folder = os.path.join(app.static_folder, 'imgassets')
#     image_files = [f for f in os.listdir(img_folder) if os.path.isfile(os.path.join(img_folder, f))]
#     return image_files
# sugnup route

# render index
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sign-up')
def sign_up():
    return render_template('schoolsignup.html')

# # render innovations.html page
# @app.route('/innovations')
# def index():
#     return render_template('innovations.html')

# # render programs.html page
# @app.route('/programs')
# def index():
#     return render_template('programs.html')

# handle signups
# @app.route('/submit', methods=['POST'])
# def submit():
#     if request.method == 'POST':
#         email = request.form['email']

#         # Send the email
#         send_email(email)

#         # You can redirect to a "Thank you" page or do any other desired action
#         return "Thank you for signing up!"

# def send_email(email):
#     # Setup email parameters
#     smtp_server = "your_smtp_server.com"
#     smtp_port = 587  # Replace with the correct port for your SMTP server
#     smtp_username = "your_email@example.com"
#     smtp_password = "your_email_password"
#     recipient_email = "recipient@example.com"  # Replace with the recipient's email

#     # Create an EmailMessage
#     message = EmailMessage()
#     message.set_content(f"New sign-up with email: {email}")
#     message["Subject"] = "New Sign-Up"
#     message["From"] = smtp_username
#     message["To"] = recipient_email

#     try:
#         # Connect to the SMTP server and send the email
#         with smtplib.SMTP(smtp_server, smtp_port) as server:
#             server.starttls()
#             server.login(smtp_username, smtp_password)
#             server.send_message(message)
#     except Exception as e:
#         print(f"Email sending failed: {str(e)}")


if __name__ == '__main__':
    app.run(debug=True)
