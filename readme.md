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
py manage.py createsuperuser
```

## Services 
