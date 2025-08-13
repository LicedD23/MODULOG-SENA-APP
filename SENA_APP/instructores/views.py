from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from .models import Instructor
from django.shortcuts import get_object_or_404

from instructores.forms import InstructorForm
from django.views import generic
from django.contrib import messages
from django.views.generic.edit import FormView


# Create your views here.
def instructores(request):
    lista_instructores = Instructor.objects.all().values()
    template = loader.get_template('lista_instructores.html')
    context= {
        'lista_instructores': lista_instructores,
        'total_instructores': lista_instructores.count(),
    }
    return HttpResponse (template.render(context, request))

def detalle_instructor(request, instructor_id):
    instructor = get_object_or_404(Instructor, id=instructor_id)
    cursos_coordinados = instructor.cursos_coordinados.all()
    cursos_impartidos = instructor.cursos_impartidos.all()
    template = loader.get_template('detalle_instructor.html')
    
    context = {
        'instructor': instructor,
        'cursos_coordinados': cursos_coordinados,
        'cursos_impartidos': cursos_impartidos,
    }
    
    return HttpResponse(template.render(context, request))

class InstructorFormView(FormView):
    template_name ='Crear_instructor.html'
    form_class=InstructorForm
    success_url = "../instructores/"
    

def form_valid(self,form):
    instructor=form.save()
    
    #Agregar mensaje de exito
    messages.success(
        self.request,
        f'El instructor {instructor.nombre} {instructor.apellido} ha sido registrado exitosamente.',
    )
    
    return super().form_valid(form)

def form_invalid(self, form):
        messages.error(
            self.request, 
            'Por favor, corrija los errores en el formulario.'
        )
        return super().form_invalid(form)



