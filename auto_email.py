"""
This script sends an email using the SMTP protocol. 
It connects to the Gmail SMTP server, 
authenticates using the provided credentials, 
and sends an email to the specified recipient.
"""

import os
import sys
import getpass
import smtplib
from pathlib import Path
from smtplib import SMTP_SSL
from dotenv import load_dotenv # 
from email.mime.text import MIMEText

# Host configuration
HOST: str = "smtp.gmail.com"
# PORT configuration
PORT: int = 587

# Load environment variables from .env file
load_dotenv()

# Define the sender and recipient email addresses
SENDER = os.environ["SENDER"]
# For one recipient
# RECIPIENT = os.environ["RECIPIENT"]

# Fo r multiple recipients, split the string by comma
RECIPIENT = os.getenv("RECIPIENT").split(",")

PASSWORD = os.environ["GMAIL_APP_PASSWORD"]

# Create the email message
MESSAGE: Path = Path("email_message.txt").read_text(encoding="utf-8")

# Establish the SMTP connection server
smtp = smtplib.SMTP(HOST, PORT)


# Status code of the response and the response message received from the server
status_code, response = smtp.ehlo()
print(f"Status code: {status_code}, Response: {response.decode()}")

# Confirm status
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