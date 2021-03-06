from django.urls import path

from user.views import UserEditBalanceView, UserListView

app_name = 'user'

urlpatterns = [
    path('list/', UserListView.as_view(), name='list'),
    path('edit-balance/', UserEditBalanceView.as_view(), name='edit-balance'),
]
