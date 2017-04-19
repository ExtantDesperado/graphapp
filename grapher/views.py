from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Function

# Create your views here.
def grapher(request):
    function = get_object_or_404(Function, pk=2)
    return render(request, 'grapher/graph_page.html', {'function': function})