from testapp.models import post
from django import template
register=template.Library()

@register.simple_tag()
def total_posts():
    return post.objects.count()

@register.inclusion_tag('testapp/tags.html')
def show_latest_posts(count=3):
    latest_posts=post.objects.order_by('-publish')[:count]
    return {'latest_posts':latest_posts}

from django.db.models import  Count
@register.assignment_tag
def most_commented_posts(count=4):
    return post.objects.annotate(most_comments=Count('comments')).order_by('most_comments')[:count]