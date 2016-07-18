from django.shortcuts import render
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext
#from connect.firmador import _entregaFirma
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def user_login(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/terminal/')
        else:
            messages.error(request, 'Usuario o Clave incorrecta')
            return render_to_response('login/login.html', context_instance=RequestContext(request))
    return render_to_response('login/login.html', context_instance=RequestContext(request))


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')