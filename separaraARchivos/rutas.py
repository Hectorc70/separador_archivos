
import os

from tkinter import filedialog


class Rutas:
    def __init__(self):
        self.abrir = filedialog.askdirectory()
        self.archivos_py = list()

    def recuperar_archivos(self):
        archivos_py   = list()
        archivos_xlsx = list()
        archivos_pdf = list()
        archivos_jpg = list()
        archivos_png = list()

        #self.guardar = filedialog.asksaveasfilename()
        #self.ext = tipo_ext
        for ruta, carpetas, documentos in os.walk(self.abrir):

            for archivo in documentos:
                rutas = ruta.replace("/","\\") + "\\" + archivo


                archivo_extencion = archivo.split('.')[-1]


                if archivo_extencion == 'py':
                    print("rutas Archivos PYTHON cargadas")

                    self.archivos_py.append(rutas)
                return self.archivos_py

        print("--Termino--")
