from django.shortcuts import redirect, render
from django.http import HttpResponse
from tidbit.models import *

def home_page(request):
    variables = {}
    return render(request, 'home.html', variables)

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    variables = {
        'list': list_
    }
    return render(request, 'list.html', variables)

def new_list(request):
    list_ = List.objects.create()
    Entry.objects.create(text=request.POST['item_text'], story_list=list_)
    return redirect('/lists/%d/' % (list_.id,))

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Entry.objects.create(text=request.POST['item_text'], story_list=list_)    
    return redirect('/lists/%d/' % (list_.id,))