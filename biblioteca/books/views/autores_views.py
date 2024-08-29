from django.shortcuts import render
from datetime import date

from books.models import Autor

def autores_view(request):
    autores = Autor.objects.all()

    context = {
        "autores": autores,
        "titulo": "Esto es una prueba en página de autores"
    }

    return render(request, "autores/autores.html", context)

def autor_detail(request, id):
    autores = [
        {
            "id":1,
            "nombre": "Antonio",
            "f_nac": date(1980,8,1)
        },
        {
            "id":2,
            "nombre": "Felipe",
            "f_nac": date(1985,10,1)
        },
        {
            "id":3,
            "nombre": "Matilde",
            "f_nac": date(1990,10,1)
        },
    ]

    context = {
        "autor":None,
    }

    for autor in autores:
        if autor["id"] == id:
            context["autor"] = autor

    return render(request,"autores/autor_detail.html",context)