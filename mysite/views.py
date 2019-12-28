from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy




class Indexview(TemplateView):
    template_name = 'index.html'

class aboutView(TemplateView):
    template_name = 'File.html'

class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class= UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'

