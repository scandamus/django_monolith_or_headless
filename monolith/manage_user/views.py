from django.views import generic
from django.contrib.auth.models import User
from django.views.generic import ListView


class IndexView(generic.TemplateView):
    template_name = "index.html"


class UserListView(ListView):
    model = User
    template_name = 'list_user.html'
    context_object_name = 'users'
