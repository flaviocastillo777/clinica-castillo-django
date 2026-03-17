from django.shortcuts import render, redirect, get_object_or_404
from .models import Medico, Paciente
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

# LISTAR Y FILTRAR MÉDICOS
def lista_medicos(request):
    # Uso de filtros ORM: búsqueda por especialidad si existe el parámetro 'esp' [cite: 24]
    especialidad_query = request.GET.get('esp')
    if especialidad_query:
        medicos = Medico.objects.filter(especialidad__icontains=especialidad_query)
    else:
        medicos = Medico.objects.all()
    return render(request, 'medicos/lista.html', {'medicos': medicos})

# CREAR MÉDICO
def crear_medico(request):
    if request.method == 'POST':
        # Captura de datos del formulario [cite: 25]
        nombre = request.POST.get('nombre')
        especialidad = request.POST.get('especialidad')
        email = request.POST.get('email')
        
        Medico.objects.create(nombre=nombre, especialidad=especialidad, email=email)
        messages.success(request, "Médico registrado exitosamente.")
        return redirect('lista_medicos')
    return render(request, 'medicos/formulario.html')

# EDITAR MÉDICO
def editar_medico(request, pk):
    medico = get_object_or_404(Medico, pk=pk)
    if request.method == 'POST':
        medico.nombre = request.POST.get('nombre')
        medico.especialidad = request.POST.get('especialidad')
        medico.email = request.POST.get('email')
        medico.save()
        return redirect('lista_medicos')
    return render(request, 'medicos/formulario.html', {'medico': medico})

# ELIMINAR MÉDICO
def eliminar_medico(request, pk):
    medico = get_object_or_404(Medico, pk=pk)
    if request.method == 'POST':
        medico.delete()
        return redirect('lista_medicos')
    return render(request, 'medicos/confirmar_eliminar.html', {'objeto': medico})

# LISTAR Y FILTRAR PACIENTES
def lista_pacientes(request):
    # Filtro ORM: Búsqueda por RUT o Nombre [cite: 24]
    q = request.GET.get('q')
    if q:
        pacientes = Paciente.objects.filter(nombre__icontains=q) | Paciente.objects.filter(rut__icontains=q)
    else:
        pacientes = Paciente.objects.all()
    return render(request, 'pacientes/lista.html', {'pacientes': pacientes})

# CREAR PACIENTE
def crear_paciente(request):
    medicos = Medico.objects.all() # Para el select del formulario
    if request.method == 'POST':
        medico_id = request.POST.get('medico')
        medico_instancia = get_object_or_404(Medico, id=medico_id)
        
        Paciente.objects.create(
            nombre=request.POST.get('nombre'),
            rut=request.POST.get('rut'),
            fecha_nacimiento=request.POST.get('fecha_nacimiento'),
            medico_asignado=medico_instancia
        )
        return redirect('lista_pacientes')
    return render(request, 'pacientes/formulario.html', {'medicos': medicos})

# EDITAR PACIENTE
def editar_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    medicos = Medico.objects.all()
    if request.method == 'POST':
        medico_id = request.POST.get('medico')
        paciente.medico_asignado = get_object_or_404(Medico, id=medico_id)
        paciente.nombre = request.POST.get('nombre')
        paciente.rut = request.POST.get('rut')
        paciente.fecha_nacimiento = request.POST.get('fecha_nacimiento')
        paciente.save()
        return redirect('lista_pacientes')
    return render(request, 'pacientes/formulario.html', {'paciente': paciente, 'medicos': medicos})

# ELIMINAR PACIENTE
def eliminar_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        paciente.delete()
        return redirect('lista_pacientes')
    return render(request, 'pacientes/confirmar_eliminar.html', {'objeto': paciente})
