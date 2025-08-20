# forms.py - VERSIÓN CORREGIDA
from django import forms
from programas.models import Programa
from instructores.models import Instructor
from aprendices.models import Aprendiz
from .models import Asistencia

class AsistenciaForm(forms.ModelForm):
    # CORRECCIÓN 1: Usar nombres consistentes (todo en minúscula para seguir convención Django)
    codigo = forms.ModelChoiceField(
        queryset=Programa.objects.all(), 
        label="Código del programa", 
        help_text="Ingrese el codigo del programa de formacion."
    )
    aprendiz = forms.ModelChoiceField(
        queryset=Aprendiz.objects.all(), 
        label="Nombre del aprendiz", 
        help_text="Ingrese el nombre del aprendiz."
    )
    instructor = forms.ModelChoiceField(
        queryset=Instructor.objects.all(), 
        label="Nombre del instructor", 
        help_text="Ingrese el nombre del instructor que dicto la clase."
    )
    cantidad_horas = forms.IntegerField(
        label="Cantidad de horas", 
        help_text="Ingrese la cantidad de horas de asistencia del aprendiz.",
        min_value=1  # MEJORA: Validación adicional
    )
    observaciones = forms.CharField(
        max_length=500, 
        label="Observaciones", 
        help_text="Ingrese las observaciones del aprendiz.", 
        required=False,
        widget=forms.Textarea(attrs={'rows': 3})  # CORRECCIÓN 2: Widget aplicado directamente
    )
    fecha_inicio = forms.DateField(
        label="Fecha de inicio", 
        help_text="Ingrese la fecha de inicio de la clase.",
        widget=forms.DateInput(attrs={'type': 'date'})  # CORRECCIÓN 2: Widget aplicado directamente
    )
    fecha_fin = forms.DateField(
        label="Fecha de fin", 
        help_text="Ingrese la fecha de fin de la clase.", 
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'})  # CORRECCIÓN 2: Widget aplicado directamente
    )
    estado = forms.ChoiceField(  # CORRECCIÓN 1: nombre en minúscula
        choices=Asistencia.ESTADO_CHOICES, 
        label="Estado", 
        help_text="Ingrese el estado de la asistencia."
    )

    class Meta:
        model = Asistencia
        fields = ['codigo', 'aprendiz', 'instructor', 'cantidad_horas', 'observaciones', 'fecha_inicio', 'fecha_fin', 'estado']
        # CORRECCIÓN 3: Eliminamos widgets de aquí porque ya los definimos arriba

    def clean(self):
        cleaned_data = super().clean()
        # CORRECCIÓN 4: Nombres consistentes (minúscula)
        codigo = cleaned_data.get('codigo')
        aprendiz = cleaned_data.get('aprendiz')
        instructor = cleaned_data.get('instructor')
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')
        
        # MEJORA: Validaciones más específicas
        errors = []
        
        if not codigo:
            errors.append('El código del programa es obligatorio.')
        
        if not aprendiz:
            errors.append('El aprendiz es obligatorio.')
            
        if not instructor:
            errors.append('El instructor es obligatorio.')
        
        # MEJORA: Validar que fecha_fin no sea anterior a fecha_inicio
        if fecha_inicio and fecha_fin:
            if fecha_fin < fecha_inicio:
                errors.append('La fecha de fin no puede ser anterior a la fecha de inicio.')
        
        if errors:
            raise forms.ValidationError(errors)
        
        return cleaned_data

    def save(self, commit=True):
        # CORRECCIÓN 5: Usar el método correcto de ModelForm
        asistencia = super().save(commit=False)
        
        # Aquí puedes hacer cualquier procesamiento adicional si es necesario
        # Los campos se asignan automáticamente desde cleaned_data
        
        if commit:
            asistencia.save()
        
        return asistencia

class BusquedaAsistenciaForm(forms.Form):
    codigo=forms.CharField(
        max_length=100,
        required=False,
        label="Consultar Fichas de Caracterización",
        widget=forms.TextInput(attrs={
            'placeholder': 'Buscar por ficha...',
            'class': 'form-control'
        })
    )
    aprendiz = forms.CharField(
        max_length=100,
        required=False,
        label="Consultar Aprendiz",
        widget=forms.TextInput(attrs={
            'placeholder': 'Buscar por nombre...',
            'class': 'form-control'
        })
    )
