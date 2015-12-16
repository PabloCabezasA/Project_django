from django.shortcuts import render
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext
from connect.firmador import _entregaFirma
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
xml_token='<?xml version="1.0"?><getToken><item><Semilla>002024309352</Semilla></item>'
xml_token+='</getToken>'
# Create your views here.
def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        respuesta,xml_enviado =_entregaFirma(xml_token)
        return render_to_response('index_project/index.html',{'respuesta':respuesta,'xml':xml_enviado},context_instance=RequestContext(request))
    return render(request, 'index_project/angular_tuto.html')    

def login(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/curso1/')
        else:
            messages.error(request, 'Usuario o Clave incorrecta')
            return render_to_response('login/login.html', context_instance=RequestContext(request))
    return render_to_response('login/login.html', context_instance=RequestContext(request))
