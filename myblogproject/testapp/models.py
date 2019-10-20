from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager

# Create your models here.

class Manager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

class post(models.Model):
    STATUS_CHOICES=(('draft','Draft'),('published','Published'))
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=256,unique_for_date='publish')
    author=models.ForeignKey(User,related_name='blog_posts')
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    create_on=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    objects=Manager()
    tags=TaggableManager()


    class meta:
        ordering = ('-publish',)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_details',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),
                                            self.slug])



class comments(models.Model):
    Post=models.ForeignKey(post,related_name="comments")
    name=models.CharField(max_length=256)
    email=models.EmailField()
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    class meta:
        ordering=('-created')
    def __str__(self):
        return 'commented by {} on {}'.format(self.name,self.Post)
