from django.shortcuts import render,get_object_or_404
from testapp.models import post
from taggit.models import Tag
from django.core.paginator import PageNotAnInteger,EmptyPage,Paginator
from testapp.forms import sharebyemail,commentsform
# Create your views here.
def postlist(request,tag_slug=None):
    post_list=post.objects.all()
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        post_list=post_list.filter(tags__in=[tag])
        print(post_list,"postlisttttttttttttttttt")
    paginator=Paginator(post_list,2)
    page_number=request.GET.get('page')

    try:
        print('Try block pagesssssssssssssssssss')
        post_list=paginator.page(page_number)
    except PageNotAnInteger:
        print('PAGE NOT INTEGER block pagesssssssssssssssssss',paginator.num_pages)
        post_list=paginator.page(1)
    except EmptyPage:
        print('eMPTY PAGE block pagesssssssssssssssssss')
        post_list=paginator.page(paginator.num_pages)
    print(post_list,"finalllllllllllllllll")

    return render(request,'testapp/post_list.html',{"post_list":post_list,"tag":tag})

# from django.views.generic import ListView
# class page(ListView):
#     model = post
#     paginate_by = 3
from django.core.mail import send_mail
def shareemail(request,id):
    post_list=get_object_or_404(post,id=id,status='published')
    sent=False
    to = "mani"
    if request.method=='POST':
        form=sharebyemail(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            sent=True
            to=cd['to']
            subject = "{} {} recommended to read u to read {}".format(cd['name'], cd['email'], post_list.title)
            post_url=request.build_absolute_uri(post_list.get_absolute_url())
            message="Read post: at \n {} \n\n{} comments:\n{}".format(post_url,cd['name'],cd['comments'])
            send_mail(subject,message,"mani@gmail.com",[cd['to']])
    form=sharebyemail()
    return render(request,"testapp/shareemail.html",{"post":post_list,"form":form,"sent":sent,"email":to})



def post_detail(request,year,month,day,sl):
    obj=get_object_or_404(post,publish__year=year,
                          status='published',
                          publish__month=month,
                          publish__day=day,
                          slug=sl)

    comments=obj.comments.filter(active=True)
    csubmit=False
    if request.method=='POST':
        form=commentsform(request.POST)
        if form.is_valid():
            new_cmnt=form.save(commit=False)
            new_cmnt.Post=obj
            new_cmnt.save()
            csubmit=True
    else:
        form=commentsform()
    return render(request,"testapp/post_detail.html",{'obj':obj,"comments":comments,"form":form,"csubmit":csubmit})
