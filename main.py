import django_setup
from myapp.models import User, Task

#funcs

def create_a_user(name):
    User.objects.create(username = name)

def get_user_by_name(name):
    return User.objects.get(username = name)

def add_task(taskname, description, username):
    task = Task(
        taskname = taskname,
        description = description,
        user = get_user_by_name(username)
    ).save()

def get_users_tasks(username):
    user = get_user_by_name(username)
    return Task.objects.filter(user = user.id).all()

