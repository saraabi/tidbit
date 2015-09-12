from django.shortcuts import redirect, render
from django.http import HttpResponse
from tidbit.models import *

def home_page(request):
    if request.method == 'POST': 
        Entry.objects.create(text=request.POST['item_text'])
        return redirect('/')
    items = Entry.objects.all()
    variables = {
        'items': items,
    }
    return render(request, 'home.html', variables)
