source env/bin/activate

python manage.py runserver
python manage.py makemigrations
python manage.py migrate

python manage.py shell

python manage.py shell < create_data.py

#CREAMOS INSTANCIAS DE BIBLIOTECA
from biblioteca.models import Autor
Autor.objects.create()

for autor in autores:
    autor.save()

for editorial in editoriales:
    editorial.save()

for libro in libros:
    libro.save()

#SI CIERRO EL PROGRAMA Y LO VULEVO A REINICAR PARA VOLVER A TENER LAS INSTANCIAS
autores = Autor.objects.all()
editoriales = Editorial.objects.all()

#CREACIÓN USUARIO
python manage.py createsuperuser

usuario: davidmarti
contraseña: 123456