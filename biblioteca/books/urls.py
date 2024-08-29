from django.shortcuts import render
from django.urls import path

from .views import (
    editoriales_view,
    autores_view,
    autor_detail,
    libros_view,
    editorial_create,
    editorial_detail
)

app_name = "books"

urlpatterns = [
    path("editoriales/", editoriales_view, name="editorial_list"),
    path("editoriales/detalle/<int:id>", editorial_detail, name="editorial_detail"),
    path("editoriales/create", editorial_create, name="editorial_create"),
    path("autores/", autores_view, name="autor_list"),
    path("autores/<int:id>", autor_detail, name="autor_detail"),
    path("libros/", libros_view, name="libros_list"),
] 