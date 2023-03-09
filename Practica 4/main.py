# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 23:54:21 2023

@author: Manuel

Algoritmos de planificacion
"""

from planificadores.planificadores import Planificadores 
from menu.menu import Menu

if __name__ == "__main__":
    file_path = input("Ingrese el path del archivo de procesos: ")
    menu = Menu(file_path)
    menu.menu_principal()

