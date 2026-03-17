
# 🏥 Sistema de Gestión Clínica Castillo - v1.0

Este proyecto es una aplicación web robusta desarrollada con **Django** y **PostgreSQL** para la gestión interna de una clínica médica. Permite administrar el cuerpo docente (médicos) y las fichas de pacientes, integrando seguridad, filtros avanzados de base de datos y una interfaz moderna.

## 🚀 Características Principales
- **CRUD Completo:** Gestión de Médicos y Pacientes (Crear, Leer, Actualizar, Eliminar).
- **Base de Datos Relacional:** Implementación en PostgreSQL con integridad referencial.
- **Consultas ORM:** Sistema de búsqueda y filtrado por nombre, RUT o especialidad.
- **Interfaz Premium:** Diseño responsivo basado en Bootstrap 5, Google Fonts (Inter) e Iconos.
- **Seguridad:** Protección contra ataques CSRF en todos los formularios.
- **Calidad de Software:** Pruebas unitarias automatizadas para validación de modelos.

---

## 🛠️ Requisitos e Instalación

### 1. Requisitos Previos
- Python 3.10 o superior.
- PostgreSQL instalado y en ejecución.

### 2. Configuración del Entorno
Clona el repositorio o sitúate en la carpeta del proyecto y ejecuta:

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno
# En Windows:
venv\Scripts\activate
# En Mac/Linux:
source venv/bin/activate

# Instalar dependencias
pip install django psycopg2-binary
```

### 3. Configuración de Base de Datos
Crea una base de datos en PostgreSQL llamada `clinica_db` y actualiza las credenciales en `core/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'clinica_db',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

### 4. Migraciones y Datos
```bash
# Sincronizar modelos con la DB
python manage.py makemigrations
python manage.py migrate

# Crear acceso al panel administrativo
python manage.py createsuperuser
```

---

## 🧪 Ejecución de Pruebas (Tests)
Para garantizar que el sistema cumple con las reglas de negocio, se han implementado 6 validaciones automáticas. Ejecútalas con:

```bash
python manage.py test
```



---

## 🖥️ Guía de Uso
1. Inicia el servidor: `python manage.py runserver`
2. Accede a `http://127.0.0.1:8000/`
3. Navega a **Médicos** para registrar a los profesionales.
4. Navega a **Pacientes** para crear fichas médicas vinculadas a los doctores disponibles.

---

## 👥 Flavio Castillo - 2026

---

### 💡 Nota Técnica sobre la Arquitectura
El sistema sigue el patrón **MVT (Model-View-Template)**, asegurando una separación clara entre la lógica de negocio en PostgreSQL y la capa de presentación en el navegador.

