from django import forms 
from .models import Asistencia

class AsistenciaForm(forms. Form):
    Codigo = forms.CharField(max_length=100, label="Código del programa", help_text="Ingrese el codigo del programa de formacion.")
    aprendiz = forms.CharField(max_length=100, label="Nombre del aprendiz", help_text="Ingrese el nombre del aprendiz.")
    instructor = forms.CharField(max_length=100, label="Nombre del instructor", help_text="Ingrese el nombre del instructor que dicto la clase.")
    cantidad_horas = forms.IntegerField(label="Cantidad de horas", help_text="Ingrese la cantidad de horas de asistencia del aprendiz.")
    observaciones = forms.CharField(max_length=500, label="Observaciones", help_text="Ingrese las observaciones del aprendiz.", required=False)
    fecha_inicio = forms.DateField(label="Fecha de inicio", help_text="Ingrese la fecha de inicio de la clase.")
    fecha_fin = forms.DateField(label="Fecha de fin", help_text="Ingrese la fecha de fin de la clase.", required=False)
    estado = forms.ChoiceField(choices=Asistencia.ESTADO_CHOICES, label="Estado", help_text="Ingrese el estado de la asistencia.")
    
    class Meta:
        model = Asistencia
        fields = '__all__'
        
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
            'observaciones': forms.Textarea(attrs={'rows': 3}),
        }

    def clean(self):
        cleaned_data = super().clean()
        codigo = cleaned_data.get('codigo')
        aprendiz = cleaned_data.get('aprendiz')
        instructor = cleaned_data.get('instructor')
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')

        if not codigo or not aprendiz or not instructor or not fecha_inicio:
            raise forms.ValidationError("Todos los campos obligatorios son requeridos.")

        if fecha_fin and fecha_inicio and fecha_fin <= fecha_inicio:
            raise forms.ValidationError("La fecha de fin debe ser posterior a la fecha de inicio.")

        return cleaned_data