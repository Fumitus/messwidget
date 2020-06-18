## Homework

### Task:

"""
Here is a quick coding challenge. We tried to make it as simple as possible so we could see how you write code, solve problems and most importantly - how you THINK.

Create a backend service for support live chat widget. It's not necessary to code frontend of the widget, but we will need some sort of client to see backend service in action.

Features we would like to see in a widget:

 -  Live typing indication

 -  Sent/Delivered/Seen statuses

 -  Per session chat history

Technical implementation is mostly up to you, just one requirement use Python and please don’t use third party integrations (don’t use Pusher ;) ) 

After you are done, add all source code with instructions on how to run the application to the Github repository and email us a link.

Our deadline is one week from now.

Don't worry if you will not complete all features listed above, do as much as you can in that time period.
"""

## Description and strategy

I created basic Flask web application for testing. BLOG accepts messages and after `Submit` button is pressed this message is recorded to data base and message about new post is Flashed. By `default` new message have status `do not seen` and this info is kept in data base column `seen`. 
BLOG have a message status descripton line: `Person read message: False` after `False` is pressed status is changed to `Person read message: True` and message about message was read is flashed.

* My idea was to catch Flashed messages using `requests`library. Command `(venv) python track_with_requests.py` starts the request and had to return message in the terminal about new post - Idea failed.
* My idea was to indicate typing using `tkinter` library. Command `(venv) python typing.py` starts typing indicator, but I do not know how to implement this funtion to the microweb I created - Idea failed.


# Follow steps below to reproduce my project.

My OS is Ubuntu 18.4

### Clone GitHub repository
use command below to do it:

```
git clone https://github.com/Fumitus/messwidget.git
```
### Create virtual environment and activate it 

From command line navigate to `messwidget` folder. You can use command below to do it:
```
cd /path/to/messwidget
```

From command line create virtualenvironment and activate it. You can use command below to do it:
```
virtualenv -p /usr/bin/python3 venv %% source venv/bin/activate
```

### Install python modules used for a project

With virtualenvironment activated install requirements.txt to downloand and install python modules used for a project. You can use command below to do it:
```
pip install -r requirements.txt
```

### Run Flask Data Base migration commands

Listed commands will initiate new sqlite data base in your system. Cloned repository contains `migration` folder with info about data base. Run command bellow to initiate new sqlite data base:

```
flask db upgrade
```
flask 

### Run Flask microblog

`.fklaskenv` contain info about variables needed to run Flask microblog. You can use command below to do it:
```
flask run
```
