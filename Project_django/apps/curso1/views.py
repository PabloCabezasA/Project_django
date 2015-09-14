from django.shortcuts import render, render_to_response, HttpResponseRedirect,get_object_or_404, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from Project_django.apps.curso1.models import autor_autor, autor_autor_obras
from Project_django.apps.curso1 import forms
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib import messages
# Create your views here.

def index(request,value=None,*args,**kwargs):
    obras = []
    if request.method == 'GET':
        option = request.GET['category_id'] if request.GET else False
        if option:
            obras = autor_autor_obras.objects.filter(autor_id = option)
    else:
        autores = autor_autor.objects.all()
    autores = autor_autor.objects.all()
    return render_to_response('curso1/index.html',{'autores': autores,'obras':obras},context_instance=RequestContext(request))


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

def autor_autor_form(request, autor_id=False):
    article = False
    if autor_id:
        article = get_object_or_404(autor_autor, pk=autor_id)
    if request.method == 'POST':
        if article:
            form = autor_autor_form(request.POST, request.FILES, instance=article)
        else:
            form = autor_autor_form(request.POST)
        if form.is_valid():
            new_persona = form.save()
            return render(request, 'curso1/autor_autor_view.html',
                   {'form': form})
    else:
        if article:
            form = autor_autor_form(instance=article)
        else:
            form = autor_autor_form()
    return render(request, 'curso1/autor_autor_view.html', {'form': form})

def autor_autor_list(request):
    autor_obj = autor_autor.objects
    lista_autores = autor_obj.all()
    return render_to_response('curso1/autor_autor_list.html', {'lista_autores': lista_autores},
    context_instance=RequestContext(request))

class AddAuthorView(CreateView):
    template_name = 'curso1/autor_autor_view.html'
    model = autor_autor
    form_class = forms.autor_autor_form

    def get_context_data(self, **kwargs):
        ctx = super(AddAuthorView, self).get_context_data(**kwargs)
        if self.request.POST:
#            ctx['form'] = forms.autor_autor_form(self.request.POST, self.request.FILES)
            ctx['inlines'] = forms.AutorObraFormSet(self.request.POST, self.request.FILES)
        else:
#            ctx['form'] = forms.autor_autor_form()
            ctx['inlines'] = forms.AutorObraFormSet()
        return ctx

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['inlines']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.object.get_absolute_url())  # assuming your model has ``get_absolute_url`` defined.
        else:
            return self.render_to_response(self.get_context_data(form=form))

class ListAuthorView(ListView):
    template_name = 'curso1/autor_autor_list.html'
    model = autor_autor

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, name=self.args[0])
        return Book.objects.filter(publisher=self.publisher)    

class EditAuthorView(UpdateView):
    model = autor_autor
    template_name = 'curso1/autor_autor_view.html'
    form_class = forms.autor_autor_form
#    success_url = reverse_lazy('autor_autor_list')

    def get_context_data(self, **kwargs):
        ctx = super(EditAuthorView, self).get_context_data(**kwargs)
        if self.request.POST:
            ctx['form'] = forms.autor_autor_form(self.request.POST, self.request.FILES, instance=self.object)
            ctx['inlines'] = forms.AutorObraFormSet(self.request.POST, self.request.FILES,instance=self.object)        
        else:
            ctx['form'] = forms.autor_autor_form(instance=self.object)
            ctx['inlines'] = forms.AutorObraFormSet(instance=self.object)
        return ctx
    
    def form_valid(self, form):
        context = self.get_context_data()
        form = context['form']
        formset = context['inlines']
        if form.is_valid():
            self.object = form.save()
            formset.instance = self.object
            if formset.is_valid():
                formset.save()
            return redirect(self.object.get_absolute_url())  # assuming your model has ``get_absolute_url`` defined.
        else:
            return self.render_to_response(self.get_context_data(form=form))

class DetailAuthorView(DetailView):
    model = autor_autor
    template_name = 'curso1/autor_autor_detalle.html'
    form_class = forms.autor_autor_form

    def get_context_data(self, **kwargs):
        ctx = super(DetailAuthorView, self).get_context_data(**kwargs)
        ctx['lista_videos'] = autor_autor_obras.objects.filter(autor_id = self.object.id)
        return ctx
    
class DeleteAutorView(DeleteView):
    model = autor_autor
    template_name = 'curso1/autor_autor_list.html'
    success_url='/curso1/autor_autor_list'

    def get_success_url(self):
        res = super(DeleteAutorView, self).get_success_url()
        """
        Redirect to the page listing all of the proxy urls
        """
        return res

    
    def get(self, *args, **kwargs):
        """
        This has been overriden because by default
        DeleteView doesn't work with GET requests
        """
        return self.delete(*args, **kwargs)
    