from django.shortcuts import render
from django.views.generic import DeleteView,DetailView,UpdateView,CreateView,ListView
from testapp.models import student
from django.core.urlresolvers import reverse_lazy

# Create your views here.
class listview(ListView):
    model = student

class details(DetailView):
    model = student

class create(CreateView):
    model = student
    fields =('name','eno','sal','eaddr')

class update(UpdateView):
    model = student
    fields = ('name','sal')

class delete(DeleteView):
    model = student
    success_url = reverse_lazy('list')
