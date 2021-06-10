

import os

import shutil
from tkinter import *
from tkinter import filedialog


from interfaz import UI_In
from rutas import Rutas





class Extenciones(UI_In,Rutas):
    """Exteniones de archivos"""


    def __init__(self):
        UI_In.__init__(self)
        Rutas.__init__(self)
        self.recuperar_archivos()


        #self.ext = self.textos


    def copiar_archivos_py(self):
        self.crear_entrada_datos()

        self.ruta_destino = None

        for ruta_ori in self.archivos_py:
            #shutil.move(ruta, self.ruta_destino

            print("soy la ruta desde la clase RUTAS: ", ruta_ori)
            print("soy la extencion desde EXTENCIONES: ", ruta_ori)

extencion = Extenciones()
extencion.copiar_archivos_py()
