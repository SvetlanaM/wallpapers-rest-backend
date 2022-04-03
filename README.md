# Wallpapers - Dagmar Šimková 

![Wallpapers - Dagmar Šimková]()

> **Wallpapers - Dagmar Šimková is an app for the artists where she can post 
her images into mobile app.**

### Technologies

- Django 1.11
- Python 3.6
- PostgreSQL
- HTML5, CSS3, JavaScript, jQuery

## Quick Start

1.  Create own virtual environment 
```
$ python3 -m venv venv
```

and then activate the environment.

2.  Clone repository

```
$ git clone https://github.com/SvetlanaM/wallpapers_backend.git
```

3.  Install requirements from the project:

```
$ pip install -r requirements.txt
```

4.  Create own database settings as a new custom database under
    existing configuration in the settings.py file.
    
5.  Run database migrations:
```
$ ./manage.py migrate --database="your database name in settings file"
```

6.  Create own admin super user:
```
$ ./manage.py createsuperuser --database="your database name in settings file"
```

7.  Run the app:
```
$ ./manage.py runserver
```

## Branches
Create a new branch which is following the rules:
*develop_githubusername*

Do not push to the master branch. 