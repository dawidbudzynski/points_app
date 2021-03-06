from django.contrib import admin
from django.urls import include, path

from user.views import UserListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', UserListView.as_view(), name='homepage'),
    path('user/', include('user.urls'))
]
