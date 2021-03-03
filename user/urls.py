from django.urls import path

from user.views import UserListView

app_name = 'user'

urlpatterns = [
    path('list/', UserListView.as_view(), name='list'),
]
