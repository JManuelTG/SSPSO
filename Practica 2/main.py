import os 
import random 
import shutil

def siwtch_chars(path):
    out_lst = []
    new_word = ""
    letters = "abcdefghijklmnopqrstuvwxyz"

    for element in os.listdir(path):
        new_path =  os.path.join(path, element)
        if os.path.isdir(new_path):
            siwtch_chars(new_path)
        else:
            if new_path.endswith(".txt"):
                with open(new_path,"r+") as file:
                    for line in file:
                        for word in line.split(" "):
                            for char in word:
                                if char.isnumeric():
                                    char = random.choice(letters)
                                elif char.isalpha():
                                    char = random.randint(1,9)
                                new_word = new_word + str(char)
                            out_lst.append(new_word)
                            new_word = ""
                    file.seek(0)
                    file.write(" ".join(x for x in out_lst))
                    out_lst = []

       

if __name__ == "__main__":

    directorio_original = './Archivos'
    directorio_copia = './Copias'
    shutil.copytree(directorio_original, directorio_copia)
    
    siwtch_chars(directorio_copia)