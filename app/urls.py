from django.contrib import admin
from django.urls import include, path

from user.views import HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='homepage'),
    path('user/', include('user.urls'))
]
