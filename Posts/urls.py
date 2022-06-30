from django.urls import path
from . import views

urlpatterns = [

    path("postFormulario" , views.postFormulario , name = 'postFormulario'),
    path('post_lista/<pk>', views.PostDetail.as_view() , name = 'post_detail'),
    path('post/borrar/<pk>', views.DeletePost.as_view(), name = "post_borrar"),
    path('post/list/' , views.PostList.as_view(), name = "post_lista"),
    path('post/edicion/<pk>', views.UpdatePost.as_view(), name ="post_edit"),
    


]

 