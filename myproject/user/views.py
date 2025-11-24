from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import cook




def cook_list(request):
    cookies= cook.objects.all().order_by('-date')
    return render(request, 'user/cook_list.html', {'cookies': cookies})


def cook_page(request, slug):
    cookie = cook.objects.get(slug=slug)
    return render(request, 'user/cook_page.html', {'cookie': cookie})
  