from django.contrib import admin
from django.urls import path
from serviceapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', checkService),
    path('check/', checkToken), 
     path('forgot-password/', forgot_password, name='forgot_password'),
]