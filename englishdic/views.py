from django.shortcuts import render,redirect
from .models import Dic
from .forms import DicForm
import requests
from pydictionary import *

# Create your views here.
def index(request):
    if request.method == 'POST':
        form  = DicForm(request.POST)
        form.save()
    items = Dic.objects.all()
    words = []
    for item in items:
        dict = Dictionary(item)
      
        data={
            'id':item.id,
            'word': item.word,
            'meaning': dict.meanings(),
            'synonyms': dict.synonyms(),
            'antonyms': dict.antonyms(),
        }
        # meaning = dict.meanings()
        # mean = dict.print_meanings()
        words.append(data)
    # print(mean)
   
    form = DicForm()

    return render(request,'index.html',{'form':form,'items':items,'words':words})

def delete(request, id):
    pos=Dic.objects.get(id=id)
    pos.delete()
    return redirect('/')