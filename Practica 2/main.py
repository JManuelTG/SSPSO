import os 
import random 
                   
def switch_chars(ruta_origen,ruta_destino,carpetas):
    verifica_ruta(ruta_destino)
    for ruta, directorios, archivos in os.walk(ruta_origen):
        for archivo in archivos:
            archivo_origen = os.path.join(ruta, archivo)
            if carpetas:
                archivo_rel = os.path.relpath(archivo_origen, ruta_origen)
                archivo_destino = os.path.join(ruta_destino, archivo_rel)
                verifica_ruta(os.path.dirname(archivo_destino))
            else:
                archivo_destino = os.path.join(ruta_destino, archivo)
            with open(archivo_origen, "r") as entrada, open(archivo_destino, "w") as salida:
                nuevo_contenido = ""
                contenido = "".join(entrada.readlines())
                for char in contenido:
                    if char.isnumeric():
                        char = chr(random.randint(97,122))
                    elif char.isalpha():
                        char = random.randint(0,9)
                    else: pass
                    nuevo_contenido += str(char)
                salida.write(nuevo_contenido)


def verifica_ruta(ruta_destino):
    if not os.path.exists(ruta_destino):
        os.makedirs(ruta_destino)
    return 


if __name__ == "__main__":
    carpetas = False
    ruta_origen = './Archivos'
    ruta_destino = './Copias'
    switch_chars(ruta_origen,ruta_destino,carpetas)