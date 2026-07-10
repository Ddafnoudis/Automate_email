# Title
Automate_email

# Objective
Create an script where a specific and defined email will be send to recipients for a specific period. 

# General Requirements
### How to find the HOST name and the PORT number?
In browser search bar type **<email provider> SMTP settings**

The user is asked to first set the email:
1) Turn on 2-Step Verification
2) Create an app password.
3) dotenv package needs to have a file called *.env*. This file contains the app password code. In terminal (bash):

>Note: If other type of mail is used, the user has follow the 2-step Verification process of that type of mail.

* `touch .env`
* `vim .env`
* APP_PASSWORD=16-character-password --> No spaces between characters
* SENDER email and RECIPIENT are also added to the .env file:
    - If you have only one recepient edit in .env file -->  `RECIPIENT=recipient@mail.com`
    - If multiple recipients edit in .env file --> `RECIPIENT="recipient_1@mail.com,recipient_2@mail.com"`
        - In case of multiple recipients, the *auto_email.py* needs to be edited accordingly.
* Save .env file in the same directory with the main script (auto_email.py)
* Create a message in .txt format with the message in the email
    - Format:
    Subject: Title of the Subject
    Greetings,
    Message
    Best,
    Name of the sender


### When script it's ready, how to automate the email to be sent every day?

*First way: Windows Task Scheduler*

After creating the auto_email.py script, open the Task Scheduler
set the time you want.
In Edit Action - Program/script 
`C:\Windows\System32\wsl.exe`

In Add arguments (optional):
`-e /home/user/path_to/bin/python3 /home/user/path/to/script.py`

*Second way: crontab tool*

On Linux, cron will continue running every day as long as the cron service is running. WSL isn't always running :(. 
In the terminal use a tool called *crontab*.
`crontab -e`: to select your editor --> /bin/nano (N.1)
Add this line below all comments
`MM HH * * * /your/name/path/bin/python3 /your/name/path/script.py`
Save the crontab

If you would like to check the open crontab sessions
`crontab -l`

**Note: If you need to reset the crontab in bash write this command: `crontab -r`**

# Package requirements
* secure-smtplib package: Main package for Secure SMTP and email exchanging. 
* dotenv: Read from .env file and put it into os.environ. 
**Note: Before using dotenv, create a file named .env in the same directory with the main script (auto_email.py). Then, insert the APP_PASSWORD (16-character password) to login to your email.**


# Python 
Python 3.12.13


# Useful references:
* [GuideRealm - How To Generate & Create App Password In Gmail Account- Full Guide](https://www.youtube.com/watch?v=7lXjlbYcpe4)
* [All About Python - How To Send Email In Python | Smtplib Tutorial](https://www.youtube.com/watch?v=S465v4mWsRg)
* [.env File Syntax Rules: Quoting, Comments, Multiline](https://env.dev/guides/env-file-syntax)


# Author
[Ddafnoudis](https://github.com/Ddafnoudis)