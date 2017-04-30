from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse

from .models import Function

# Create your views here.
def index(request):
    #if request.method == 'POST':
        #function = get_object_or_404(Function, name=request.POST['text'])
        #return HttpResponse(function.pk)
        #try:
        #    return HttpResponseRedirect(reverse('grapher', args=(request.POST['dropdown'],)))
        #except (KeyError):
        #    return HttpResponse()
    #else:
    return render(request, 'grapher/index.html', {'function_list': Function.objects.all()})

def grapher(request, function_id):
    function = get_object_or_404(Function, pk=function_id)
    return render(request, 'grapher/graph_page.html', {'function': function, 'function_list': Function.objects.all()})

