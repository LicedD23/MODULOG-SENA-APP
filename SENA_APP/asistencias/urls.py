from django.urls import path
from . import views
from .views import AsistenciaFormView

app_name= 'asistencias'

urlpatterns = [
    path('asistencias/', views.asistencias, name='lista_asistencias'),
    path('crear_asistencia/', AsistenciaFormView.as_view(), name='crear_asistencia'),
]
