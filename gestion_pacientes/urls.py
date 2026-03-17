from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # URLs Médicos
    path('medicos/', views.lista_medicos, name='lista_medicos'),
    path('medicos/nuevo/', views.crear_medico, name='crear_medico'),
    path('medicos/editar/<int:pk>/', views.editar_medico, name='editar_medico'),
    path('medicos/eliminar/<int:pk>/', views.eliminar_medico, name='eliminar_medico'),
    
    # URLs Pacientes
    path('pacientes/', views.lista_pacientes, name='lista_pacientes'),
    path('pacientes/nuevo/', views.crear_paciente, name='crear_paciente'),
    path('pacientes/editar/<int:pk>/', views.editar_paciente, name='editar_paciente'),
    path('pacientes/eliminar/<int:pk>/', views.eliminar_paciente, name='eliminar_paciente'),
]
