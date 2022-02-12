# Maxeco
Service based app.

## mysqlclient
[Python interface to MySQL](https://pypi.org/project/mysqlclient/)

```pip install mysqlclient```

## Connect to mysql
```python
'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'maxeco',
    'USER': 'root',
    'PASSWORD': '',
    'HOST': 'localhost',
    'PORT': '3306',
}
```

## Creating an admin user
```
python manage.py createsuperuser
```

## Services 

## Virtual environment
To install:
```
pip install virtualenv
```

To create an environment:
```
python -m venv <environment name>
```

Go to environment directory & start:
```
cd <environment name>\Scripts\
activate.bat
```

To deactive:
```
deactivate
```
