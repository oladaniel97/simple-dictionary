from django.forms import TextInput,ModelForm
from .models import Dic

class DicForm(ModelForm):
    class Meta:
        model = Dic
        fields = ['word']
        widgets = {'word': TextInput(attrs={'class': 'form-control', 'placeholder':'Search for a word'})}