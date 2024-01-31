import os
import django 

os.environ.setdefault(key=("DJANGO_SETTINGS_MODULE"), value=('mysite.settings'))
django.setup()