# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 01:25:27 2023

@author: Manue
"""

salida = []
with open('prueba2.txt', 'r') as file:
    for line in file:
        entrada = line.strip().split(",")
        componentes_ipv6 = entrada[0].split("/")[0].split(":")
        componentes_ipv4 = entrada[5].split(".")
        
        ipv6 = ":".join(str(int(componente, 16)) for componente in componentes_ipv6)
        ipv4 = ":".join(hex(int(componente))[2:] for componente in componentes_ipv4)
        
        nombre = entrada[2]
        resultado = f"{nombre}, {ipv6}, {ipv4}"
        salida.append(resultado)

with open('salida.txt', 'w') as file:
    for resultado in salida:
        file.write(resultado + '\n')
        
        