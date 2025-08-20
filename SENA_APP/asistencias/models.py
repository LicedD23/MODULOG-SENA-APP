from django.db import models

# Create your models here.

class Asistencia(models.Model):
    ESTADO_CHOICES = [
        ('SI','asistio'),
        ('NO','no asistio'),
    ]
    codigo= models.ForeignKey('programas.Programa', on_delete=models.CASCADE ,verbose_name="Código del Programa")
    aprendiz= models.ForeignKey('aprendices.Aprendiz', on_delete=models.CASCADE, verbose_name="Aprendiz")
    instructor= models.ForeignKey('instructores.Instructor', on_delete=models.CASCADE, verbose_name="Instructor",help_text="Instructor que dicto la clase")
    cantidad_horas= models.PositiveIntegerField(verbose_name="Horas de Asistencia" , help_text="Cantidad de horas de asistencia del aprendiz")
    observaciones= models.TextField(blank=True, null=True, verbose_name="Observaciones",help_text="Observaciones sobre la asistencia")
    fecha_inicio= models.DateField(verbose_name="Fecha Inicio")
    fecha_fin= models.DateField(verbose_name="Fecha Fin")
    Estado= models.CharField(max_length=2, choices=ESTADO_CHOICES, default='SI', verbose_name="Estado")
    
    def __str__(self):
        return f"{self.codigo} - {self.aprendiz}"
    
    class Meta:
        verbose_name = "Asistencia"
        verbose_name_plural = "Asistencias"