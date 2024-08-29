from django.shortcuts import render, redirect
from django.urls import reverse
from books.forms import EditorialModelFormCreate, EditorialCreate
from books.models import Editorial

def editoriales_view(request):

    editorial = Editorial.objects.all()

    context = {
        "editoriales": editorial
    }

    return render(request, "editoriales/editoriales.html", context)  

def editorial_detail(request, id):

    editorial = Editorial.objects.get(pk=id)

    context = {
        "editorial": editorial
    }

    return render(request, "editoriales/editorial_detail.html", context)

def editorial_create(request):
    if request.POST:
        form = EditorialModelFormCreate(request.POST)

        if form.is_valid():
            nueva_editorial = Editorial.objects.create(
                nombre = form.cleaned_data["nombre"],
                direccion = form.cleaned_data["direccion"],
                email = form.cleaned_data["email"],
                fecha_fundacion = form.cleaned_data["fecha_fundacion"]
            )

            #Redirecciona a la vista detalle de la neuva editorial creada
            return redirect(reverse('books:editorial_detail', kwargs={'id': nueva_editorial.pk}))
    else:
        form = EditorialModelFormCreate()
    
    context = {
        "form": form
    }

    return render(request, "editoriales/editorial_create.html", context)