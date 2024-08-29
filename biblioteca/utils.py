from django.db import models


# Modelo para Editoriales
class Editorial(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=300)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    sitio_web = models.URLField()
    fecha_fundacion = models.DateField()

    def __str__(self):
        return self.nombre


# Modelo para Autores
class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=100)
    biografia = models.TextField()
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    sitio_web = models.URLField()
    premios = models.TextField()
    foto = models.ImageField(upload_to="autores_fotos/", null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# Modelo para Libros
class Libro(models.Model):
    titulo = models.CharField(max_length=300)
    isbn = models.CharField(max_length=13, unique=True)
    fecha_publicacion = models.DateField()
    numero_paginas = models.IntegerField()
    idioma = models.CharField(max_length=100)
    portada = models.ImageField(upload_to="portadas_libros/", null=True, blank=True)
    descripcion = models.TextField()
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    autores = models.ManyToManyField(Autor)
    genero = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.titulo


# admin.py
from django.contrib import admin
from .models import Editorial, Autor, Libro


class LibroInline(admin.TabularInline):
    model = Libro.autores.through
    extra = 1


class LibroInlineForEditorial(admin.TabularInline):
    model = Libro
    extra = 1


@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ("nombre", "ciudad", "estado", "pais", "fecha_fundacion")
    search_fields = ("nombre", "ciudad", "estado", "pais")
    list_filter = ("pais", "estado", "ciudad")
    ordering = ("nombre",)
    inlines = [LibroInlineForEditorial]


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "nacionalidad", "email")
    search_fields = ("nombre", "apellido", "nacionalidad", "email")
    list_filter = ("nacionalidad",)
    ordering = ("apellido", "nombre")
    inlines = [LibroInline]


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "isbn", "fecha_publicacion", "editorial", "precio")
    search_fields = ("titulo", "isbn", "editorial__nombre")
    list_filter = ("fecha_publicacion", "editorial", "genero")
    ordering = ("titulo",)
    filter_horizontal = ("autores",)
    exclude = ("autores",)


# Crear instancias
python manage.py shell

from myapp.models import Editorial, Autor, Libro
from datetime import date

editoriales = [
    Editorial(nombre=f'Editorial {i}', direccion=f'Dirección {i}', ciudad='Ciudad', estado='Estado',
              pais='País', codigo_postal=f'0000{i}', telefono=f'123456789{i}', email=f'editorial{i}@example.com',
              sitio_web=f'http://editorial{i}.com', fecha_fundacion=date(2000+i, 1, 1))
    for i in range(1, 11)
]
Editorial.objects.bulk_create(editoriales)

autores = [
    Autor(nombre=f'Nombre {i}', apellido=f'Apellido {i}', fecha_nacimiento=date(1970+i, 1, 1), nacionalidad='Nacionalidad',
          biografia=f'Biografía del autor {i}', email=f'autor{i}@example.com', telefono=f'987654321{i}',
          sitio_web=f'http://autor{i}.com', premios=f'Premio {i}', foto=None)
    for i in range(1, 11)
]
Autor.objects.bulk_create(autores)


editoriales = Editorial.objects.all()
autores = Autor.objects.all()

libros = [
    Libro(titulo=f'Título del Libro {i}', isbn=f'123456789012{i}', fecha_publicacion=date(2010+i, 1, 1), 
          numero_paginas=100+i, idioma='Idioma', portada=None, descripcion=f'Descripción del libro {i}', 
          editorial=editoriales[i % len(editoriales)], genero='Género', precio=19.99 + i)
    for i in range(1, 11)
]
Libro.objects.bulk_create(libros)

for libro in Libro.objects.all():
    libro.autores.set(autores[:i % len(autores)])
    libro.save()
