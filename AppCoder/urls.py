from django.urls import path
from AppCoder import views

urlpatterns = [
    path('' , views.inicio, name ="Inicio"),
    path('AcercaDeNosotros' , views.acercaDeNosotros,name = "AcercaDeNosotros"),
    path('blog', views.blog , name = "Blog"),
    

]

