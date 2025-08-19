from django.template import loader
from .models import Asistencia

from django.http import HttpResponse
from asistencias.forms import AsistenciaForm
from django.views import generic
from django.contrib import messages
from django.views.generic.edit import FormView

# Create your views here.
def asistencias(request):
    lista_asistencias= Asistencia.objects.all()
    template = loader.get_template("lista_asistencias.html")
    context={
        "lista_asistencias":lista_asistencias,
        "total_asistencias":lista_asistencias.count(),
        }
    return HttpResponse(template.render(context,request))

class AsistenciaFormView(FormView):
    template_name ='crear_asistencia.html'
    form_class=AsistenciaForm
    success_url = "../asistencias/"
    

    def form_valid(self,form):
        asistencia=form.save()
        
        #Agregar mensaje de exito
        messages.success(
            self.request,
            f'La asistencia del aprendiz {asistencia.nombre} ha sido registrada exitosamente.',
        )
        
        return super().form_valid(form)

    def form_invalid(self, form):
            messages.error(
                self.request, 
                'Por favor, corrija los errores en el formulario.'
            )
            return super().form_invalid(form)
