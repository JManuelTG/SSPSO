import os 
import random 
import shutil

def siwtch_chars(path):
    out_lst = []
    new_word = ""
    letters = "abcdefghijklmnopqrstuvwxyz"
    for element in os.listdir(path):
        new_path =  os.path.join(path, element)
        if os.path.isdir(element):
            siwtch_chars(element)
        else:
            if new_path.endswith(".txt"):
                with open(new_path,"r") as file:
                    for line in file:
                        for word in line.split(" "):
                            for char in word:
                                if char.isnumeric():
                                    char = random.choice(letters)
                                elif char.isalpha():
                                    char = random.randint(1,9)
                                else:
                                    pass
                                new_word = new_word + str(char)
                            out_lst.append(new_word)
                            new_word = ""
                    with open(new_path,"a") as out:
                        out.write("\n=================\n" + " ".join(x for x in out_lst))
                    out_lst = []
            else:
                pass
       

if __name__ == "__main__":
    directorio_original = './Archivos'
    directorio_copia = './Copias'
    shutil.copytree(directorio_original, directorio_copia)
    
    siwtch_chars(directorio_copia)