from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Function

# Create your views here.
def index(request):
    return render(request, 'grapher/index.html', {'function_list': Function.objects.all()})

def grapher(request, function_id):
    function = get_object_or_404(Function, pk=function_id)
    return render(request, 'grapher/graph_page.html', {'function': function, 'function_list': Function.objects.all()})