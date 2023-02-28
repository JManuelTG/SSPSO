import os 
import random 
import shutil

def siwtch_chars(path):
    out_lst = []
    new_word = ""
    for element in os.listdir(path):
        new_path =  os.path.join(path, element)
        if os.path.isdir(new_path):
            siwtch_chars(new_path)
        else:
            if new_path.endswith(".txt"):
                with open(new_path,"r+") as file:
                    for line in file:
                        for char in line:
                            if char.isnumeric():
                                char = chr(random.randint(97,122))
                            elif char.isalpha():
                                char = random.randint(0,9)
                            else: pass
                            new_word = new_word + str(char)
                        out_lst.append(new_word)
                        new_word = ""
                    file.seek(0)
                    file.write("".join(x for x in out_lst))
                    out_lst = []
            else: pass
                    

def paths():
    directorio_original = './Archivos'
    directorio_copia = './Copias'
    shutil.copytree(directorio_original, directorio_copia,dirs_exist_ok=True)
    return directorio_copia


if __name__ == "__main__":
  
    siwtch_chars(paths())