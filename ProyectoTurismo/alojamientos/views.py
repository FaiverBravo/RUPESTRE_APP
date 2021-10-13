from django.shortcuts import render

from alojamientos.models import Alojamiento, Categoria, Post
# Create your views here.


def alojamientos(request):

    alojamientos=Alojamiento.objects.all()
    categorias=Categoria.objects.all()
    posts=Post.objects.all()
    
    return render(request, "alojamientos/alojamientos.html", {
        "alojamientos": alojamientos,
        "categorias": categorias,
        "posts": posts
        })

def alojamiento_detalle(request):

    # alojamientos=Alojamiento.objects.all()
    # categorias=Categoria.objects.all()
    # posts=Post.objects.all()
    
    # return render(request, "alojamientos/alojamientos.html", {
    #     "alojamientos": alojamientos,
    #     "categorias": categorias,
    #     "posts": posts
      #  })
    return render(request, "alojamientos/alojamiento_detalle.html", {
        
    })

def categoria(request, categoria_id):

    categoria=Categoria.objects.get(id=categoria_id)
   # posts=Post.objects.filter(categorias=categoria)
    return render(request, "alojamientos/categoria.html", {'categoria':categoria, })    