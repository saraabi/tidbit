from django.shortcuts import redirect, render
from django.http import HttpResponse
from tidbit.models import *

def home_page(request):
    variables = {}
    return render(request, 'home.html', variables)

def view_list(request):
    items = Entry.objects.all()
    variables = {
        'items': items,
    }
    return render(request, 'list.html', variables)

def new_list(request):
    Entry.objects.create(text=request.POST['item_text'])
    return redirect('/lists/the-only-story-in-the-world/')