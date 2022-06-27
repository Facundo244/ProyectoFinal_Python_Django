from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import  DetailView
from django.views.generic.edit import DeleteView
from Posts.models import Post
from Posts.forms import FormularioPost  , BuscarPost



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


class PostView(DetailView):
    model = Post
    template_name = 'Post/template/postView.html'


def postLista(request):

    postAbuscar = request.GET.get('titulo', None)

    if postAbuscar is not None:

        post = Post.objects.filter(titulo = postAbuscar)
    else:
        post = Post.objects.all()

    form = BuscarPost()
    return render (request , 'Posts/template/postLista.html' , {'form':form , 'post': post})





class EliminarPost(DeleteView):
    model = Post
    template_name = "Post/template/postConfirmDelete.html"
    success_url = reverse_lazy('Blog')



