from django.shortcuts import render     #clase 13

def libros_view(request):
    return render(request, "libros/libros.html")
