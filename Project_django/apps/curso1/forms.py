from django.forms import ModelForm
from Project_django.apps.curso1 import models
from django.forms.models import inlineformset_factory


class autor_autor_form(ModelForm):
    class Meta:
        model = models.autor_autor
        fields = "__all__"

class autor_autor_obras_form(ModelForm):
    class Meta: 
        model = models.autor_autor_obras
        fields = "__all__"

AutorObraFormSet = inlineformset_factory(models.autor_autor,
                                        models.autor_autor_obras,
                                        can_delete=True,
                                        fields="__all__")