from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField

# Create your models here.
JOB_TYPE = (
    ('full time','full time'),
    ('part time','part time'),
)
class job(models.Model):

    title = models.CharField(max_length=100)
    #location
    job_type = models.CharField(max_length=15,choices=JOB_TYPE)
    descraption = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('category',on_delete=CASCADE)

    def __str__(self):
        return self.title

class category(models.Model):
    name = CharField(max_length=25)
    def __str__(self) -> str:
        return self.name