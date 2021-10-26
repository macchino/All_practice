import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TemplateProject.settings')
from django import setup
setup()

from TemplateApp.models import Students, Schools, Prefectures

s = Schools.objects.first()
# print(type(s))
# print(dir(s))
# print(s.prefecture.name)
# print(s.students_set)
# st = s.students_set
# print(type(st))
# print(dir(st))
# print(st.all())

from TemplateApp.models import Places, Restaurants

# p = Places.objects.first()
# print(p.restaurants.name)
# r = Restaurants.objects.first()
# print(r.place.name)

# 多対多
from TemplateApp.models import Books, Authors

b = Books.objects.first()
print(b.authors.all())

r = Authors.objects.first()
print(r.books_set.all())