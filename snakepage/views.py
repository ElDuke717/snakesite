# appname/views.py
from django.shortcuts import render
from .models import Item

# Create your views here.

def item_list(request):
    items = Item.objects.all()
    return render(request, 'appname/item_list.html', {'items': items})
