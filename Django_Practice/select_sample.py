import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TemplateProject.settings')
from django import setup
setup()

from TemplateApp.models import Person

persons = Person.objects.all()
for person in persons:
    print(person.id, person, person.salary)

# getは主キーで使う。複数結果はエラーになる
person = Person.objects.get(pk=1)
print(person, person.id)
print('*'*100
)
persons = Person.objects.filter(first_name='Taro').all()
print(persons)
print(persons[0].email)
for person in persons:
    print(person.id, person)
