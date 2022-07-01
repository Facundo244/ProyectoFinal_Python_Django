from django.contrib import admin
from django.urls import path, include



urlpatterns = [

    path('admin/', admin.site.urls),
    path('',include('AppCoder.urls')),
    path('',include("Cuenta.urls")),
    path('',include("Posts.urls")),
    
]
