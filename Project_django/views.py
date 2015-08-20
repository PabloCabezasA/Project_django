from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from connect.firmador import _entregaFirma
xml_token='<?xml version="1.0"?><getToken><item><Semilla>002024309352</Semilla></item>'
xml_token+='</getToken>'


# Create your views here.
def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        respuesta,xml_enviado =_entregaFirma(xml_token)
        return render_to_response('index_project/index.html',{'respuesta':respuesta,'xml':xml_enviado},context_instance=RequestContext(request))
    return render(request, 'index_project/index.html')    