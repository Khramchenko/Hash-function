# Модуль предоставляет следующие функции: md5(), sha1(), sha224(), sha256(), sha384 и sha512().

import hashlib
import sys
import os

#функции шифрования для алгоритмов md5 sha1 sha256.
def md5_coder(md5):
    hash_md5 = hashlib.md5()
    with open(md5, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""): #читаем по 4096 байт
            hash_md5.update(chunk)
    return hash_md5.hexdigest() # получаем зашифрованную строку символов hexdigest()
        
        
def sha1_coder(sha1):
    hash_sha1 = hashlib.sha1()
    with open(sha1, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha1.update(chunk)
    return hash_sha1.hexdigest()

def sha256_coder(sha256):
    hash_sha256 = hashlib.sha256()
    with open(sha256, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()  

def verification(func, hashfunc):
    
    if func==hashfunc:
        return "OK"
    else:
        return "FAIL"             

def main(argv):
    
    fname=argv[1]
    file_tree=argv[2]

    with open(fname, 'r') as f:
        for line in f:
            try:
                file_name, code, hash_code=line.split(' ')
            except ValueError:
                return print("Строка содержит не верное количество аргументов")
            hash_code=hash_code.strip() # strip() удаляем символ переноса строки /n strip()
            os.chdir(file_tree)         # меняем рабочую директорию
            
            if file_name in os.listdir():     # listdir() возвращает список файлов в указанной папке        
                if code=='md5':
                    print(file_name, verification(hash_code, md5_coder(file_name)))
                elif code=='sha1':
                    print(file_name, verification(hash_code, sha1_coder(file_name)))
                elif code=='sha256':
                    print(file_name, verification(hash_code, sha256_coder(file_name)))
                else:
                    print("Not valid function")
            else:
                print("NOT FOUND")

            

 
if __name__=="__main__":
    main(sys.argv) #запуск скрипта с параметрами из компандной строки
    

