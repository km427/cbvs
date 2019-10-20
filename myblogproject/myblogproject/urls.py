"""myblogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from testapp.views import postlist,post_detail,shareemail

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',postlist),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$',postlist,name='post_list_by_tag_name'),
    url(r'^(?P<id>[0-9]+)/share/$', shareemail),

    # url(r'^$',page.as_view()),
    url(r'(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<sl>[-\w]+)/$',post_detail,name='post_details')
]
