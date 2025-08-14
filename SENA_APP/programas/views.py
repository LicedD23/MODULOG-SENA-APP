from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from .models import Programa
from django.shortcuts import get_object_or_404
from programas.forms import ProgramaForm
from django.views import generic
from django.contrib import messages
from django.views.generic.edit import FormView


# Create your views here.
def programas(request):
    lista_programas = Programa.objects.all().values()
    template = loader.get_template('lista_programas.html')
    context= {
        'lista_programas': lista_programas,
        'total_programas': lista_programas.count(),
    }
    return HttpResponse (template.render(context, request))

def detalle_programa(request, programa_id):
    programa =get_object_or_404(Programa, id=programa_id)
    cursos = programa.curso_set.all().order_by('-fecha_inicio')
    template = loader.get_template('detalle_programa.html')
    context= {
        'programa': programa,
        'cursos': cursos,
    }
    return HttpResponse (template.render(context, request)) 

class ProgramaFormView(FormView):
    template_name ='crear_programa.html'
    form_class=ProgramaForm
    success_url = "../programas/"
    
    def form_valid(self,form):
        programa=form.save()
        
        #Agregar mensaje de exito
        messages.success(
            self.request,
            f'El programa {programa.nombre} ha sido registrado exitosamente.',
        )
        
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(
            self.request, 
            'Por favor, corrija los errores en el formulario.'
        )
        return super().form_invalid(form)
    
    
