import sys
import getpass
import os
import smtplib
from smtplib import SMTP_SSL
from email.mime.text import MIMEText


# Host configuration
HOST: str = "smtp.gmail.com"
# PORT configuration
PORT: int = 587

# Define the sender and recipient email addresses
SENDER: str = "dimitrios.dafnoudis@gmail.com"
RECIPIENT: str = "ddafnoudis1995@gmail.com"

# Provide password
# PASSWORD: str = getpass.getpass(input(f"Enter your email password: "))

PASSWORD: str = getpass.getpass(f"Enter your email password for {SENDER}: ")

# Create the email message
MESSAGE: str = """Subject: Test Email 
Hi,https://mail.google.com/mail/u/1/?hl=el&pli=1#inbox
This is a test email sent from Python.

Best,
Test User
"""
# Establish the SMTP connection server
smtp = smtplib.SMTP(HOST, PORT)

# Status code of the response and the response message received from the server
status_code, response = smtp.ehlo()
print(f"Status code: {status_code}, Response: {response.decode()}")

if status_code == 250:
    print("Successfully connected to the SMTP server.")

elif status_code == 421:
    print("Service not available, closing transmission channel.")
    sys.exit(1)

# Start TLS encryption for secure communication
security_status_code, security_response = smtp.starttls()
print(f"Security Status code: {security_status_code}, Security Response: {security_response.decode()}")

# Call ehlo() again after starting TLS to re-identify the client to the server
status_code, response = smtp.ehlo()

# Login to the SMTP server using email and password
login_status_code, login_response = smtp.login(SENDER, PASSWORD)
print(f"Login Status code: {login_status_code}, Login Response: {login_response.decode()}")

# Send the email
smtp.sendmail(SENDER, RECIPIENT, MESSAGE)
# Close the SMTP connection
smtp.quit()