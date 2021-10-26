import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TemplateProject.settings')
from django import setup
setup()

from TemplateApp.models import Person


Person.objects.filter(first_name='Saburo').delete()
Person.objects.filter(first_name='taro', birthday='2000-01-01').delete()
Person.objects.all().delete()
