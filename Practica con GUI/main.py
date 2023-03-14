# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 23:54:21 2023

@author: Manuel

Algoritmos de planificacion
"""
from tkinter import Tk
from app.app import App
import ttkbootstrap as ttk

if __name__ == "__main__":
    root = ttk.Window(themename="darkly")
    my_app = App(root)
    root.mainloop()


