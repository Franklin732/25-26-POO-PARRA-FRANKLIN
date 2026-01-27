"""
Dashboard de Programacion Orientada a Objetos
Adaptado por: Franklin Parra
Semana 8: Gestor de Proyectos y Tareas

Este dashboard permite organizar, visualizar y ejecutar proyectos y scripts
relacionados con la materia de Programacion Orientada a Objetos.

Caracteristicas:
- Navegacion por semanas y temas
- Visualizacion de codigo de scripts
- Ejecucion de scripts en tiempo real
- Gestion de proyectos POO
- Documentacion integrada
"""

import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path


class DashboardPOO:
    """Clase para gestionar el dashboard de proyectos POO"""
    
    def __init__(self):
        """Inicializa el dashboard con la ruta base"""
        self.ruta_base = os.path.dirname(__file__)
        self.proyecto_raiz = os.path.dirname(self.ruta_base)
        self.semanas_disponibles = self._obtener_semanas()
        
    def _obtener_semanas(self):
        """Obtiene las carpetas de semanas disponibles en el proyecto"""
        semanas = {}
        try:
            for item in os.listdir(self.proyecto_raiz):
                ruta_item = os.path.join(self.proyecto_raiz, item)
                if os.path.isdir(ruta_item) and (item.startswith('semana_') or item.startswith('Semana')):
                    semanas[item] = ruta_item
        except Exception as e:
            print(f"Error al obtener semanas: {e}")
        return semanas
    
    def mostrar_codigo(self, ruta_script):
        """Muestra el contenido de un archivo Python"""
        ruta_absoluta = os.path.abspath(ruta_script)
        try:
            with open(ruta_absoluta, 'r', encoding='utf-8') as archivo:
                codigo = archivo.read()
                print(f"\n{'='*60}")
                print(f"Codigo de: {os.path.basename(ruta_script)}")
                print(f"{'='*60}\n")
                print(codigo)
                print(f"\n{'='*60}\n")
                return codigo
        except FileNotFoundError:
            print("[ERROR] El archivo no se encontro.")
            return None
        except Exception as e:
            print(f"[ERROR] Error al leer el archivo: {e}")
            return None
    
    def ejecutar_codigo(self, ruta_script):
        """Ejecuta un script Python en una nueva ventana"""
        try:
            if os.name == 'nt':  # Windows
                subprocess.Popen(['cmd', '/k', 'python', ruta_script])
            else:  # Unix-based systems
                subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
            print("[OK] Script ejecutado exitosamente")
        except Exception as e:
            print(f"[ERROR] Error al ejecutar el codigo: {e}")
    
    def listar_proyectos(self):
        """Lista todos los proyectos y semanas disponibles"""
        print("\n" + "="*60)
        print("PROYECTOS Y SEMANAS DISPONIBLES")
        print("="*60)
        
        if not self.semanas_disponibles:
            print("No hay semanas disponibles")
            return
        
        for nombre, ruta in sorted(self.semanas_disponibles.items()):
            print(f"\n[CARPETA] {nombre}/")
            try:
                archivos_py = [f for f in os.listdir(ruta) if f.endswith('.py')]
                carpetas = [f for f in os.listdir(ruta) if os.path.isdir(os.path.join(ruta, f)) and not f.startswith('_')]
                
                if archivos_py:
                    print("   Archivos Python:")
                    for archivo in archivos_py:
                        print(f"      - {archivo}")
                
                if carpetas:
                    print("   Carpetas:")
                    for carpeta in carpetas:
                        print(f"      - {carpeta}/")
            except Exception as e:
                print(f"   Error al listar: {e}")
    
    def mostrar_menu_principal(self):
        """Muestra el menu principal del dashboard"""
        print("\n" + "="*60)
        print("DASHBOARD POO - SEMANA 8")
        print("="*60)
        print("\nOpciones disponibles:")
        print("1 - Explorar Semanas")
        print("2 - Listar todos los Proyectos")
        print("3 - Ver Documentacion")
        print("4 - Acerca del Dashboard")
        print("0 - Salir")
        print("-"*60)
        return input("Selecciona una opcion: ")
    
    def mostrar_semanas(self):
        """Muestra el menu de seleccion de semanas"""
        if not self.semanas_disponibles:
            print("[ADVERTENCIA] No hay semanas disponibles")
            return
        
        semanas_list = sorted(self.semanas_disponibles.items())
        
        while True:
            print("\n" + "="*60)
            print("SELECCIONAR SEMANA")
            print("="*60)
            
            for i, (nombre, ruta) in enumerate(semanas_list, 1):
                print(f"{i} - {nombre}")
            print("0 - Regresar al menu principal")
            
            try:
                opcion = int(input("\nSelecciona una semana: "))
                if opcion == 0:
                    break
                elif 1 <= opcion <= len(semanas_list):
                    nombre_semana, ruta_semana = semanas_list[opcion - 1]
                    self.mostrar_submenu_semana(nombre_semana, ruta_semana)
                else:
                    print("[ADVERTENCIA] Opcion no valida")
            except ValueError:
                print("[ADVERTENCIA] Por favor ingresa un numero valido")
    
    def mostrar_submenu_semana(self, nombre_semana, ruta_semana):
        """Muestra las opciones de una semana especifica"""
        while True:
            print("\n" + "="*60)
            print(f"SEMANA: {nombre_semana}")
            print("="*60)
            
            # Obtener carpetas
            try:
                carpetas = [f for f in os.listdir(ruta_semana) 
                           if os.path.isdir(os.path.join(ruta_semana, f)) 
                           and not f.startswith('_')]
                archivos_py = [f for f in os.listdir(ruta_semana) if f.endswith('.py')]
            except Exception as e:
                print(f"[ERROR] Error: {e}")
                return
            
            # Mostrar opciones
            opciones = {}
            numero = 1
            
            # Agregar archivos Python
            if archivos_py:
                print("\n[ARCHIVOS] Archivos Python:")
                for archivo in archivos_py:
                    print(f"{numero} - {archivo}")
                    opciones[numero] = ('archivo', os.path.join(ruta_semana, archivo))
                    numero += 1
            
            # Agregar carpetas
            if carpetas:
                print("\n[CARPETAS] Carpetas:")
                for carpeta in carpetas:
                    print(f"{numero} - {carpeta}/")
                    opciones[numero] = ('carpeta', os.path.join(ruta_semana, carpeta))
                    numero += 1
            
            print(f"\n0 - Regresar")
            
            try:
                opcion = int(input("\nSelecciona una opcion: "))
                if opcion == 0:
                    break
                elif opcion in opciones:
                    tipo, ruta = opciones[opcion]
                    if tipo == 'archivo':
                        self.procesar_archivo(ruta)
                    else:
                        self.mostrar_submenu_carpeta(ruta)
                else:
                    print("[ADVERTENCIA] Opcion no valida")
            except ValueError:
                print("[ADVERTENCIA] Por favor ingresa un numero valido")
    
    def mostrar_submenu_carpeta(self, ruta_carpeta):
        """Muestra los scripts en una carpeta"""
        while True:
            print("\n" + "="*60)
            print(f"CARPETA: {os.path.basename(ruta_carpeta)}")
            print("="*60)
            
            try:
                scripts = [f for f in os.listdir(ruta_carpeta) if f.endswith('.py')]
                
                if not scripts:
                    print("No hay archivos Python en esta carpeta")
                    break
                
                for i, script in enumerate(scripts, 1):
                    print(f"{i} - {script}")
                print("0 - Regresar")
                
                opcion = int(input("\nSelecciona un script: "))
                if opcion == 0:
                    break
                elif 1 <= opcion <= len(scripts):
                    ruta_script = os.path.join(ruta_carpeta, scripts[opcion - 1])
                    self.procesar_archivo(ruta_script)
                else:
                    print("[ADVERTENCIA] Opcion no valida")
            except ValueError:
                print("[ADVERTENCIA] Por favor ingresa un numero valido")
            except Exception as e:
                print(f"[ERROR] Error: {e}")
                break
    
    def procesar_archivo(self, ruta_archivo):
        """Procesa la visualizacion y ejecucion de un archivo"""
        while True:
            print("\n" + "="*60)
            print(f"ARCHIVO: {os.path.basename(ruta_archivo)}")
            print("="*60)
            
            print("\nOpciones:")
            print("1 - Ver Codigo")
            print("2 - Ejecutar Script")
            print("3 - Ver Informacion del archivo")
            print("0 - Regresar")
            
            opcion = input("\nSelecciona una opcion: ")
            
            if opcion == '0':
                break
            elif opcion == '1':
                self.mostrar_codigo(ruta_archivo)
            elif opcion == '2':
                self.ejecutar_codigo(ruta_archivo)
            elif opcion == '3':
                self.mostrar_info_archivo(ruta_archivo)
            else:
                print("[ADVERTENCIA] Opcion no valida")
    
    def mostrar_info_archivo(self, ruta_archivo):
        """Muestra informacion del archivo"""
        try:
            stat_info = os.stat(ruta_archivo)
            tamano = stat_info.st_size
            fecha_mod = datetime.fromtimestamp(stat_info.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
            
            print(f"\n{'='*60}")
            print("INFORMACION DEL ARCHIVO")
            print(f"{'='*60}")
            print(f"Nombre: {os.path.basename(ruta_archivo)}")
            print(f"Ruta: {ruta_archivo}")
            print(f"Tamano: {tamano} bytes")
            print(f"Ultima modificacion: {fecha_mod}")
            print(f"{'='*60}\n")
        except Exception as e:
            print(f"[ERROR] Error al obtener informacion: {e}")
    
    def mostrar_documentacion(self):
        """Muestra documentacion sobre el dashboard"""
        print("\n" + "="*60)
        print("DOCUMENTACION DEL DASHBOARD")
        print("="*60)
        print("""
Este Dashboard POO fue creado como parte de la Semana 8.

CARACTERISTICAS PRINCIPALES:
- Exploracion de semanas y proyectos
- Visualizacion de codigo Python
- Ejecucion de scripts en tiempo real
- Gestion organizada de proyectos POO
- Informacion detallada de archivos

COMO USAR:
1. Selecciona "Explorar Semanas" en el menu principal
2. Elige una semana para ver sus contenidos
3. Navega por carpetas y archivos
4. Visualiza el codigo o ejecuta scripts

ESTRUCTURA DEL PROYECTO:
- semana_X/: Contiene ejercicios de cada semana
- main.py: Archivos principales de cada semana
- UNIDAD X/: Contenido original del repositorio

CONTACTO:
Estudiante: Franklin Parra
Materia: Programacion Orientada a Objetos
Fecha: 2025-2026
        """)
        print("="*60)
    
    def mostrar_acerca(self):
        """Muestra informacion acerca del dashboard"""
        print("\n" + "="*60)
        print("ACERCA DEL DASHBOARD")
        print("="*60)
        print("""
DASHBOARD POO v1.0
Gestor de Proyectos y Tareas

CREADO POR:
Nombre: Franklin Parra
Materia: Programacion Orientada a Objetos
Semestre: 2025-2026
Semana: 8

DESCRIPCION:
Este dashboard es una herramienta adaptada basada en el proyecto
original de: https://github.com/snogales-uea/2525-PROGRAMACION-ORIENTADA-A-OBJETOS

Se ha personalizado para facilitar la organizacion y gestion de
proyectos relacionados con la programacion orientada a objetos.

CARACTERISTICAS:
- Interfaz de linea de comandos intuitiva
- Navegacion jerarquica de proyectos
- Visualizacion de codigo en tiempo real
- Ejecucion de scripts
- Gestion de multiples semanas

ADAPTACIONES REALIZADAS:
- Integracion con la estructura del proyecto personal
- Mejora de la interfaz de usuario
- Adicion de funcionalidades nuevas
- Documentacion mejorada
- Mejor manejo de errores

REQUISITOS:
- Python 3.6+
- Sistema Operativo: Windows, Linux o macOS

USO:
    python Dashboard.py
        """)
        print("="*60)
    
    def ejecutar(self):
        """Ejecuta el dashboard"""
        while True:
            opcion = self.mostrar_menu_principal()
            
            if opcion == '0':
                print("\nHasta luego!")
                break
            elif opcion == '1':
                self.mostrar_semanas()
            elif opcion == '2':
                self.listar_proyectos()
            elif opcion == '3':
                self.mostrar_documentacion()
            elif opcion == '4':
                self.mostrar_acerca()
            else:
                print("[ADVERTENCIA] Opcion no valida. Por favor, intenta de nuevo.")


def main():
    """Funcion principal"""
    dashboard = DashboardPOO()
    dashboard.ejecutar()


if __name__ == "__main__":
    main()
