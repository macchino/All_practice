import os
from django.db.models import aggregates

from django.db.models.aggregates import Min

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TemplateProject.settings')
from django import setup
setup()

from TemplateApp.models import Students

# print(Students.objects.all())

# 件数
# print(Students.objects.count())
# print(Students.objects.filter(name='太郎').count())

# 件数、最大値、最小値、平均値、合計
from django.db.models import Count, Max, Avg, Sum

# print(Students.objects.aggregate(Count('pk'), Max('pk'), Min('pk'), Avg('pk'), Sum('age')))
# aggregate_students = Students.objects.aggregate(counted_pk=Count('pk'),max_pk= Max('pk'), min_pk=Min('pk'), avg_pk=Avg('pk'), sum_pk=Sum('age'))
# print(aggregate_students)

# GROUPE BY
# print(Students.objects.values('name').annotate(
# max_id=Max('pk'), min_id=Min('pk')
# ).query)

for student in Students.objects.values('name').annotate(
    max_id=Max('pk'), min_id=Min('pk')):
    print(student['name'], student['max_id'])
