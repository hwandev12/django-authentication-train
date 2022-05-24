from django.contrib import admin
from django.urls import path, include
from authentication.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls'))
]
