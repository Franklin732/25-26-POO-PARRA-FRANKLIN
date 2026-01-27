"""
test_dashboard.py - Pruebas unitarias para el Dashboard POO

Este archivo contiene pruebas para verificar que las funciones
principales del Dashboard funcionan correctamente.
"""

import os
import sys
import unittest
from pathlib import Path

# Para hacer que el import de Dashboard funcione
sys.path.insert(0, os.path.dirname(__file__))

# Importar la clase DashboardPOO
try:
    from Dashboard import DashboardPOO
except ImportError:
    print("No se pudo importar Dashboard. Asegurate de estar en el directorio correcto.")
    sys.exit(1)


class TestDashboardPOO(unittest.TestCase):
    """Tests para la clase DashboardPOO"""
    
    def setUp(self):
        """Inicializa el dashboard para las pruebas"""
        self.dashboard = DashboardPOO()
    
    def test_inicializacion(self):
        """Prueba que el dashboard se inicializa correctamente"""
        self.assertIsNotNone(self.dashboard)
        self.assertIsNotNone(self.dashboard.ruta_base)
        self.assertIsNotNone(self.dashboard.proyecto_raiz)
    
    def test_obtener_semanas(self):
        """Prueba que se obtienen las semanas disponibles"""
        semanas = self.dashboard.semanas_disponibles
        self.assertIsInstance(semanas, dict)
        self.assertGreater(len(semanas), 0)
    
    def test_ruta_base_existe(self):
        """Prueba que la ruta base existe"""
        self.assertTrue(os.path.exists(self.dashboard.ruta_base))
    
    def test_proyecto_raiz_existe(self):
        """Prueba que la ruta del proyecto raiz existe"""
        self.assertTrue(os.path.exists(self.dashboard.proyecto_raiz))
    
    def test_semanas_tienen_rutas_validas(self):
        """Prueba que todas las semanas tienen rutas validas"""
        for nombre_semana, ruta_semana in self.dashboard.semanas_disponibles.items():
            self.assertTrue(os.path.exists(ruta_semana), 
                          f"Ruta de {nombre_semana} no existe: {ruta_semana}")
    
    def test_mostrar_codigo_archivo_inexistente(self):
        """Prueba que mostrar_codigo maneja archivos inexistentes"""
        resultado = self.dashboard.mostrar_codigo("/ruta/inexistente.py")
        self.assertIsNone(resultado)
    
    def test_archivo_dashboard_existe(self):
        """Prueba que el archivo Dashboard.py existe en semana_8"""
        ruta_dashboard = os.path.join(self.dashboard.ruta_base, "Dashboard.py")
        self.assertTrue(os.path.exists(ruta_dashboard))
    
    def test_archivo_readme_existe(self):
        """Prueba que el archivo README.md existe"""
        ruta_readme = os.path.join(self.dashboard.ruta_base, "README.md")
        self.assertTrue(os.path.exists(ruta_readme))


class TestFuncionesAuxiliares(unittest.TestCase):
    """Tests para funciones auxiliares"""
    
    def setUp(self):
        """Inicializa el dashboard"""
        self.dashboard = DashboardPOO()
    
    def test_listar_proyectos_no_error(self):
        """Prueba que listar_proyectos no lanza errores"""
        try:
            # Capturamos stdout para no imprimir durante las pruebas
            import io
            from contextlib import redirect_stdout
            
            f = io.StringIO()
            with redirect_stdout(f):
                self.dashboard.listar_proyectos()
            
            output = f.getvalue()
            self.assertIn("PROYECTOS Y SEMANAS DISPONIBLES", output)
        except Exception as e:
            self.fail(f"listar_proyectos lanzo una excepcion: {e}")
    
    def test_mostrar_info_archivo_dashboard(self):
        """Prueba mostrar informacion del archivo Dashboard.py"""
        try:
            ruta_dashboard = os.path.join(self.dashboard.ruta_base, "Dashboard.py")
            if os.path.exists(ruta_dashboard):
                # Capturamos stdout
                import io
                from contextlib import redirect_stdout
                
                f = io.StringIO()
                with redirect_stdout(f):
                    self.dashboard.mostrar_info_archivo(ruta_dashboard)
                
                output = f.getvalue()
                self.assertIn("INFORMACION DEL ARCHIVO", output)
                self.assertIn("Dashboard.py", output)
        except Exception as e:
            self.fail(f"mostrar_info_archivo lanzo una excepcion: {e}")


def ejecutar_pruebas():
    """Ejecuta todas las pruebas"""
    # Crear un test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Agregar tests
    suite.addTests(loader.loadTestsFromTestCase(TestDashboardPOO))
    suite.addTests(loader.loadTestsFromTestCase(TestFuncionesAuxiliares))
    
    # Ejecutar tests
    runner = unittest.TextTestRunner(verbosity=2)
    resultado = runner.run(suite)
    
    # Retornar si todas las pruebas pasaron
    return resultado.wasSuccessful()


if __name__ == "__main__":
    print("="*60)
    print("Ejecutando pruebas del Dashboard POO")
    print("="*60)
    
    exito = ejecutar_pruebas()
    
    print("\n" + "="*60)
    if exito:
        print("[OK] Todas las pruebas pasaron exitosamente")
    else:
        print("[ERROR] Algunas pruebas fallaron")
    print("="*60)
    
    sys.exit(0 if exito else 1)
