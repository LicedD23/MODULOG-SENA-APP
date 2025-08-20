from django.template import loader

from instructores.models import Instructor
from programas.models import Programa
from aprendices.models import Aprendiz

from .models import Asistencia

from django.http import HttpResponse
from asistencias.forms import AsistenciaForm
from django.views import generic
from django.contrib import messages
from django.views.generic.edit import FormView
from django.urls import reverse_lazy


# Create your views here.
def asistencias(request):
    lista_asistencias= Asistencia.objects.all()
    lista_aprendices = Aprendiz.objects.all()
    lista_programas = Programa.objects.all()
    template = loader.get_template("lista_asistencias.html")
    context={
        "lista_asistencias":lista_asistencias,
        "total_asistencias":lista_asistencias.count(),
        'lista_aprendices': lista_aprendices,
        'lista_programas': lista_programas,
        
        }
    return HttpResponse(template.render(context,request))

class AsistenciaFormView(generic.FormView):
    template_name ='crear_asistencia.html'
    form_class=AsistenciaForm
    success_url = "../asistencias/"
    

    def form_valid(self,form):
        form.save()
        
        #Agregar mensaje de exito
        messages.success(
            self.request,
            f'La asistencia del aprendiz  ha sido registrada exitosamente.',
        )
        
        return super().form_valid(form)

    def form_invalid(self, form):
            messages.error(
                self.request, 
                'Por favor, corrija los errores en el formulario.'
            )
            return super().form_invalid(form)

def crear_asistencia(request):
    lista_aprendices = Aprendiz.objects.all()
    lista_programas = Programa.objects.all()
    lista_instructores = Instructor.objects.all()
    template = loader.get_template('crear_asistencia.html')
    context= {
        
        'lista_aprendices': lista_aprendices,
        'lista_programas': lista_programas,
        'lista_instructores': lista_instructores,
    }
    return HttpResponse (template.render(context, request))


