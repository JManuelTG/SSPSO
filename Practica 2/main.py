import os 
import random 
                   
def copia_archivos_y_modifica_contenido(ruta_origen,ruta_destino,conservar__carpetas):
    """
    Recibe una ruta de origen, una ruta de destino y un booleano que indica si se deben preservar las carpetas
    de origen en la ruta de destino. Modifica los archivos de la ruta de origen, cambiando letras por números y
    viceversa, y los guarda en la ruta de destino.
    """
    verifica_ruta(ruta_destino)

    for ruta, directorios, archivos in os.walk(ruta_origen):
        for archivo in archivos:
            archivo_origen = os.path.join(ruta, archivo)
            
            if conservar__carpetas:
                 # Obtener la ruta relativa del archivo y crear la misma estructura de carpetas en destino
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

                    nuevo_contenido += str(char)
                salida.write(nuevo_contenido)


def verifica_ruta(ruta_destino):
    """
    Recibe una ruta de destino y verifica si la carpeta existe, si no existe la crea.
    """
    if not os.path.exists(ruta_destino):
        os.makedirs(ruta_destino)



if __name__ == "__main__":
    carpetas = False  
    ruta_origen = './Archivos'
    ruta_destino = './Copias'
    copia_archivos_y_modifica_contenido(ruta_origen,ruta_destino,carpetas)