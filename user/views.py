from django.views.generic import TemplateView
from django.views.generic.list import ListView

from user.models import User


class HomePageView(TemplateView):
    template_name = "user/home.html"


class UserListView(ListView):
    model = User

    ordering = ['last_name', 'first_name']
