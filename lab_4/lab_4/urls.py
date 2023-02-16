
from django.contrib import admin
from django.urls import path
from user.views import *

urlpatterns = [
    path('', index_view),
    path('admin/', admin.site.urls),
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
]
