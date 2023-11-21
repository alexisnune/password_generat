import string
import secrets 
import os
os.system("cls")

def contiene_mayusculos(password)->bool:
    for letra in password:
        if letra.isupper():
            return True
    return False
def contiene_simbulos(password)->bool:   
    for letra in password:
        if letra in string.punctuation:
            return True
    return False 
def generar_password(longitud,tiene_simbolos, tiene_mayusculas)->str: 
    combinacion =string.ascii_lowercase + string.digits
    
    if tiene_simbolos:
        combinacion += string.punctuation
    if tiene_mayusculas:
        combinacion += string.ascii_uppercase
        longitud_combinacion= len(combinacion)
    nuevo_password=""
    for _ in range(longitud):
        nuevo_password += combinacion[secrets.randbelow(longitud_combinacion)]
    print(combinacion)
    return nuevo_password 
if __name__ == "__main__":
    nuevo=generar_password(longitud=10,tiene_simbolos=True, tiene_mayusculas=True)
    print(f"Tiene mayusculas: {contiene_mayusculos(nuevo)}")
    print(f"Tiene simbolos: {contiene_simbulos(nuevo)}")
    print(nuevo)
           