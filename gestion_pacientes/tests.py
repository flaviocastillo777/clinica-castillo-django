from django.test import TestCase
from .models import Medico, Paciente

class ClinicaTest(TestCase):
    def setUp(self):
        self.medico = Medico.objects.create(nombre="Doc House", especialidad="Diagnóstico", email="house@clinic.com")

    def test_creacion_medico(self):
        """Validaciones para Médico"""
        self.assertEqual(self.medico.nombre, "Doc House") # Val 1
        self.assertTrue(isinstance(self.medico, Medico)) # Val 2
        self.assertEqual(str(self.medico), "Dr. Doc House - Diagnóstico") # Val 3

    def test_creacion_paciente(self):
        """Validaciones para Paciente"""
        p = Paciente.objects.create(nombre="John Doe", rut="1-9", fecha_nacimiento="1990-01-01", medico_asignado=self.medico)
        self.assertEqual(p.rut, "1-9") # Val 1
        self.assertEqual(p.medico_asignado.nombre, "Doc House") # Val 2
        self.assertIn("John", p.nombre) # Val 3
        