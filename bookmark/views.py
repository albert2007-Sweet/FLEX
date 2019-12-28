from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from bookmark.models import Bookmark
from django.core.urlresolvers import reverse_lazy

# Create your views here.

class BookMarkLV(ListView):
    model = Bookmark

class BookMarkDV(DetailView):
    model = Bookmark

class BookMarkCV(CreateView):
    model = Bookmark
    fields= ['title', 'url']
    success_url = reverse_lazy('bookmark_index')
    
class BookMarkUV(UpdateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark_index')

class BookMarkRV(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark_index')

