


# Project Description

This repo contains code for ToDo applicaion developed 
with python and pyramid framework.





## Requirements

 - [Python 3](https://www.python.org)
 - [Pyramid](https://trypyramid.com)
 - [Jinja2](https://pypi.org/project/Jinja2/)
 - [SQLAlchemy](https://www.sqlalchemy.org/)
 - [Deform](https://docs.pylonsproject.org/projects/deform/en/latest/index.html)
 - [Waitress Server](https://docs.pylonsproject.org/projects/waitress/en/latest/)
 



## Installation
The steps for runnig  the application on your operating system
are as follows: All the commands needed to be run in the terminal.

Install python 3 on your operating system. I develop this project in python 3.10

```bash
pip3 install python
```

clone the repository from the github on your system
```bash
https://github.com/slmaankhaan/todo_app.git
```
Open the folder in editior of your choice. I used Pycharm to develope
this app. Don't forget to activate the virtual environment before 
running the application by using the following command:
```bash
 source env3.10/bin/activate
```
The dependencies needed for the project are listed in the setup
.py  and requirements.txt files. In order to  install the 
dependencies if the application is not running properly use the following command:
```bash
 pip install -e . -r requirements.txt
```

In case the database is not working properly on your system, please remove
the database by using the follwing  command:
```bash
rm mysite.sqlite
```

After removing the database intialize it again with:
```bash
initialize_db development.ini
```
Once the above steps are completed run the application using the following command:
```bash
initialize_db development.ini
```

To login as a user to manage Todos enter the following credentials

```bash
username: jill
username: jill1

username: jack
password: jack2
```

To login as admin to manage users and todos enter the following 
credentials

```bash
username: admin
password: admin3
```



## UI of the app
Welcome Screen
![Welcome Screen](https://github.com/slmaankhaan/todo_app/blob/master/app_screenshots/welcome_screen.png?raw=true)

Login Screen

![Login Screen](https://github.com/slmaankhaan/todo_app/blob/master/app_screenshots/login_screen.png?raw=true)

Add item
![Add Item](https://github.com/slmaankhaan/todo_app/blob/master/app_screenshots/add_todo.png?raw=true)

Item Added
![Item added](https://github.com/slmaankhaan/todo_app/blob/master/app_screenshots/item%20added.png?raw=true)

Item Deleted
![Item Deleted](https://github.com/slmaankhaan/todo_app/blob/master/app_screenshots/item_deleted.png?raw=true)


## Lincense

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

