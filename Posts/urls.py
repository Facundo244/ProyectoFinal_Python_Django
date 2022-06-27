from django.urls import path
from . import views

urlpatterns = [

    path("postFormulario/" , views.postFormulario , name = 'postFormulario'),
    path('postConfirmDelete/' , views.EliminarPost.as_view() , name = 'postConfirmDelete'),
    path('postLista/' , views.postLista , name = 'postLista'),
    path('postView/' , views.PostView.as_view() , name = 'postView'),


]

 