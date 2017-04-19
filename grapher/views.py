from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def grapher(request):
    #template = loader.get_template('grapher/grapher.html')
    #return HttpResponse(template.render(request))
    return render(request, 'grapher/graph_page.html')