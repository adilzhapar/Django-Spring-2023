
from django.contrib import admin
from django.urls import path
from user.views import *

urlpatterns = [
    path('login/', login_view),
    path('', index_view),
    path('admin/', admin.site.urls),
    path('logout/', logout_view),
    path('register/', register_view),
]
