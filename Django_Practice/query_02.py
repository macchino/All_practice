import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TemplateProject.settings')
from django import setup
setup()

from TemplateApp.models import Students, Person

# print(Students.objects.all())

# IN
ids = [25, 26, 27]
# print(Students.objects.filter(pk__in=ids))

# contain 部分一致 遅い
# print(Students.objects.filter(name__contains='三'))

# is null
# p = Person(
#     first_name = 'JIro', last_name='Yamada',
#     birthday='2000-01-01', email='aa@mail.com',
#     salary=None, memo='mome jiro', web_site='http://jiro'
# )
# p.save()
# print(Person.objects.filter(salary__isnull=True))
# print(Person.objects.exclude(salary__isnull=True))

# print(Students.objects.exclude(name='太郎'))

# values:一部のカラムだけ取り出す
# print(Students.objects.values('name', 'age').filter(pk=14).query)

students = Students.objects.values('id', 'name', 'age')
for student in students:
    print(student['id'])

    # 並び替え(order_by)
print(Students.objects.order_by('-name', 'id'))
