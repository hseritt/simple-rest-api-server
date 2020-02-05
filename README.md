# Simple Rest API Server

This is a very simple Rest API server written using Django and the Django Rest Framework.

It has a very simple app already included called "events". It can be used with frontend JS frameworks like Angular or React. In fact, it pairs very well with my own [angular-tour-of-events](https://github.com/hseritt/angular-tour-of-events/tree/GET-Example-DjangoRF).


## Set Up

Clone project into a folder.

Install Python 3.8.1 using pyenv (see the Pyenv section on this page for notes on how to install pyenv: https://dev.prodigi.us/post/python-package-and-version-management/).

`$ pyenv install 3.8.1              # Install Python 3.8.1` \
`$ pyenv virtualenv rest-api-server # Set up a virtual environment called rest-api-server` \
`$ pyenv local rest-api-server      # Designates this space as virtual environment container` \
`$ pip install -r requirements.txt  # Installs necessary packages` 


## Run rest-api-server 

`$ python manage.py runserver` 


## View Rest API Response

In a browser go to http://localhost:8000/api/events


## How to Create an App

Change to the project folder.

```bash
$ ./manage.py startapp todo
```

Open rest_api_server/settings.py. Add the app name 'todo' to the end of INSTALLED_APPS:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'example',
    'todo',
]
```

Save the settings.py file.

Open todo/models.py and add an example model:

```python
from django.db import models


class Todo(models.Model):
    title = models.CharField('Title', max_length=50)
    description = models.TextField('Description')
    created = models.DateTimeField(auto_now_add=True)
    due = models.DateTimeField()

    def __str__(self):
        return self.title
```

We can migrate our model to the database.

```bash
$ ./manage.py makemigrations
Migrations for 'todo':
  todo/migrations/0001_initial.py
    - Create model Todo

$ ./manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, example, sessions, todo
Running migrations:
  Applying todo.0001_initial... OK
```

Add the 'Todo' model to the Django admin by opening the todo/admin.py file and adding:

```python
from django.contrib import admin
from .models import Todo


admin.site.register(Todo)
```

In the todo app folder, create a new file called serializers.py and add the following:

```python

from rest_framework import serializers, viewsets
from .models import Todo


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = [
            'title',
            'description',
            'created',
            'due',
        ]


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

```

Create an entry in rest_api_server/urls.py:

```python
...
from todo.serializers import TodoViewSet # <- Import the TodoViewSet from the serializers module.


class UserSerializer(serializers.HyperlinkedModelSerializer):
    ...


router = routers.DefaultRouter()
...
router.register(r'todos', TodoViewSet) # <- Register the TodoViewSet as 'todos'
```

Start the Django development server:

```bash
$ ./manage.py runserver
```

In the web browser go to http://localhost:8000/api/todos/. There will be an empty list showing for todos but you can add them either with the Rest API interface or using the [Django admin console](http://localhost:8000/admin/).

To login to the Django development server, use admin / admin.
