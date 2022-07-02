from django.http import  HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import  ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView , UpdateView
from Posts.models import Post
from Posts.forms import FormularioPost 
from django.contrib.auth.mixins import LoginRequiredMixin





# Create your views here.

@login_required
def postFormulario(request):

    if request.method == 'POST':

        miFormulario = FormularioPost(request.POST , files = request.FILES)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data
            mensaje = miFormulario.cleaned_data['titulo']

            posts = Post(titulo=informacion ['titulo'] , subtitulo=informacion ['subtitulo'] , texto = informacion['texto'] , autor=informacion['autor'])
            posts.save()

            return render( request , 'AppCoder/template/inicio.html' , {'mensaje': f'Se creo el post "{mensaje}" con exito!! '})

        else:

            return render( request , 'Posts/template/postFormulario.html', {'miFormulario':miFormulario}) 

    miFormulario = FormularioPost() 
    return render(request, "Posts/template/postFormulario.html", {'miFormulario':miFormulario})  





class DeletePost(LoginRequiredMixin ,DeleteView):

    model = Post
    template_name = 'Posts/template/post_confirm_delete.html'
    success_url = reverse_lazy('post_lista')


class UpdatePost(LoginRequiredMixin ,UpdateView):

    model= Post
    fields = ['titulo' , 'subtitulo' , 'texto']
    template_name = 'Posts/template/post_update.html'
    success_url = reverse_lazy('post_lista')


class PostDetail(LoginRequiredMixin ,DetailView):
    model = Post
    template_name = 'Posts/template/post_detail.html'


class PostList(LoginRequiredMixin , ListView):

    model = Post
    template_name = 'Posts/template/post_lista.html'















        









