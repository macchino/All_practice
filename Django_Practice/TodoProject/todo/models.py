from django.db import models
from django.db.models.fields import CharField

# Create your models here.
PRIORIRY = (
    ('bt1', 'high'),
    ('bt2', 'normal'),
    ('bt3', 'usual')
)

class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices = PRIORIRY
    )
    duedate = models.DateField()

    def __str__(self):
        return self.title
