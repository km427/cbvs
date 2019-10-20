from django.db import models
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=60)
    eno=models.IntegerField()
    sal=models.IntegerField()
    eaddr=models.CharField(max_length=60)

    def get_absolute_url(self):
        return reverse('home')



