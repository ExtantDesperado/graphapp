from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse

from .models import Function

# Create your views here.
def index(request):
    return render(request, 'grapher/index.html', {'function_list': Function.objects.all()})

def grapher(request, function_id):
    function = get_object_or_404(Function, pk=function_id)
    try:
        x1 = request.GET['x1']
        x2 = request.GET['x2']
        y1 = request.GET['y1']
        y2 = request.GET['y2']
    except (KeyError):
        return render(request, 'grapher/graph_page.html', {'function': function, 'function_list': Function.objects.all()})
    else:
        return render(request, 'grapher/graph_page.html', {'function': function, 'function_list': Function.objects.all(), 'x1': x1, 'x2': x2, 'y1': y1, 'y2': y2})

def input(request):
    return render(request, 'grapher/input.html', {'function_list': Function.objects.all()})
    
def create(request):
    if not request.POST['name']:
        return render(request, 'grapher/input.html', {'function_list': Function.objects.all(), 'error_message': "Enter a function name.", 'prev_script': request.POST['javascript']})
    if not request.POST['javascript']:
        return render(request, 'grapher/input.html', {'function_list': Function.objects.all(), 'error_message': "Enter function JavaScript.", 'prev_name': request.POST['name']})
    try:
        Function.objects.get(name=request.POST['name'])
    except Function.DoesNotExist:
        newFunction = Function(name=request.POST['name'], script=request.POST['javascript'])
        newFunction.save()
        return HttpResponseRedirect(reverse('grapher', args=(newFunction.pk,)))
    else:
        return render(request, 'grapher/input.html', {'function_list': Function.objects.all(), 'error_message': "Function with that name already exists.", 'prev_script': request.POST['javascript']})

def operations(request):
    return render(request, 'grapher/operations.html', {'function_list': Function.objects.all()})

def dictionary(request):
    return render(request, 'grapher/dictionary.html', {'function_list': Function.objects.all()})