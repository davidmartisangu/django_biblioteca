from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from books.forms import EditorialModelFormCreate, EditorialCreate
from books.models import Editorial
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class EditorialListView(ListView):
    model = Editorial
    template_name = "editoriales/EditorialList.html"
    context_object_name = "editoriales" #para que en el html cuando el for de editorial sepa que es editoriales


class EditorialDetailView(DetailView):
    model = Editorial
    template_name = "editoriales/EditorialDetail.html"
    context_object_name = "editorial"


class EditorialCreateView(CreateView):
    model = Editorial
    template_name = "editoriales/EditorialCreate.html"
    success_url = reverse_lazy("editorial:list")
    fields=["nombre", "direccion","ciudad","estado","pais", "codigo_postal", "telefono", "email",
            "sitio_web", "fecha_fundacion"]


class EditorialUpdateView(UpdateView):
    model = Editorial
    template_name = "editoriales/EditorialUpdate.html"
    success_url = reverse_lazy("editorial:list")
    fields=["nombre", "direccion","ciudad","estado","pais", "codigo_postal", "telefono", "email",
        "sitio_web", "fecha_fundacion"]


class EditorialDeleteView(DeleteView):
    model = Editorial
    template_name = "editoriales/EditorialDelete.html"
    success_url = reverse_lazy("editorial:list")


# def editoriales_view(request):

#     editorial = Editorial.objects.all()

#     context = {
#         "editoriales": editorial
#     }

#     return render(request, "editoriales/editoriales.html", context)  

# def editorial_detail(request, id):

#     editorial = Editorial.objects.get(pk=id)

#     context = {
#         "editorial": editorial
#     }

#     return render(request, "editoriales/editorial_detail.html", context)

# def editorial_create(request):
#     if request.POST:
#         form = EditorialModelFormCreate(request.POST)

#         if form.is_valid():
#             nueva_editorial = Editorial.objects.create(
#                 nombre = form.cleaned_data["nombre"],
#                 direccion = form.cleaned_data["direccion"],
#                 email = form.cleaned_data["email"],
#                 fecha_fundacion = form.cleaned_data["fecha_fundacion"]
#             )

#             #Redirecciona a la vista detalle de la neuva editorial creada
#             return redirect(reverse('books:editorial_detail', kwargs={'id': nueva_editorial.pk}))
#     else:
#         form = EditorialModelFormCreate()
    
#     context = {
#         "form": form
#     }

#     return render(request, "editoriales/editorial_create.html", context)