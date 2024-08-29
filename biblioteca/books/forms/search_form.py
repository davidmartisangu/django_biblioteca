from django import forms


class SearchForm(forms.Form):
    searching = forms.CharField(
        label="Introduce las palabras claves para la busqueda",
        max_length=100
    )