# Title
Automate_email

# Objective
Create an script where a specific and defined email will be send to recipients for a specific period. 

# Theory
### How to find the HOST name and the PORT number?
In browser search bar type **<email provider> SMTP settings**

The user is asked to first set the email:
1) Turn on 2-Step Verification
2) Create an app password.
3) dotenv package needs to have a file called *.env*. This file contains the app password code. In terminal (bash):

* `touch .env`
* `vim .env`
* APP_PASSWORD=16-character-password --> No spaces between characters
* Save .env file in the same directory with the main script (auto_email.py)

### When script it's ready, how to automate the email to be sent every day?
In the terminal use a tool called *crontab*.
`crontab -e`: to select your editor --> /bin/nano (N.1)
Add this line below all comments
`MM HH * * * /your/name/path/bin/python3 /your/name/path/script.py`
Save the crontab 

**Note: If you need to reset the crontab in bash write this command: `crontab -r`**



1) What is SMTP?
# Requiremnents
* secure-smtplib package: Main package for Secure SMTP and email exchanging. 
* dotenv: Read from .env file and put it into os.environ. 
**Note: Before using dotenv, create a file named .env in the same directory with the main script (auto_email.py). Then, insert the APP_PASSWORD (16-character password) to login to your email.**


# Python 
Python 3.12.13


# Useful references:
* [GuidRealm - How To Generate & Create App Password In Gmail Account- Full Guide](https://www.youtube.com/watch?v=7lXjlbYcpe4)
* [All About Python - How To Send Email In Python | Smtplib Tutorial](https://www.youtube.com/watch?v=S465v4mWsRg)


# Author
Ddafnoudis