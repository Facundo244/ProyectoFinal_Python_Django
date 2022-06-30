from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Posts.models import Post




@login_required
def acercaDeNosotros(request):
    return render(request, 'AppCoder/template/acerca_De.html')


@login_required
def blog(request):
    posts = Post.objects.all()
    return render(request , 'Posts/template/post_lista.html' , {'posts':posts})



def inicio(request):
    
    if request.user.is_authenticated:
        return render(request, "AppCoder/template/padre.html") 
    else:
        return render(request, "AppCoder/template/padre.html")



