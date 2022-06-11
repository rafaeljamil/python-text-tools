import random as rand
import rot

def minusculo(texto):
    new_string = texto.lower()
    return new_string


def maiusculo(texto):
    new_string = texto.upper()
    return new_string

def aleatorio(texto):
    # TODO: embaralha as letras
    old_string = texto.split()
    new_string = ""
    if len(old_string) > 1:
        while len(old_string) > 0:
            n = rand.randint(0, len(old_string)-1)
            new_string += old_string[n] + " "
            old_string.remove(old_string[n])
        new_string = "".join(new_string)
    else:
        my_list = list(old_string[0])
        while len(my_list) > 0:
            n = rand.randint(0, len(my_list)-1)
            new_string += my_list[n]
            my_list.remove(my_list[n])

    return new_string

def esses(texto):
    # TODO: adiciona S ou ES no fim das palavras
    old_string = texto.split()
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_string = ""
    for word in old_string:
        if word[-1] in vowels:
            new_string += word + 's '
        else:
            new_string += word + 'es '
    
    return new_string

def camelo(texto):
    # TODO: alterna entre maiúsculas e minúsculas
    new_string = ""
    for i in range(len(texto)):
        if i % 2 == 0:
            new_string += maiusculo(texto[i])
        else:
            new_string += minusculo(texto[i])
    
    return new_string

def espaco(texto):
    # TODO: adiciona espaço entre cada letra
    new_string = ""
    for i in range(len(texto)):
        new_string += texto[i] + " "
    return new_string

def espelho(texto):
    # TODO: inverte o texto
    new_string = ""
    n = len(texto)-1
    #print(n)
    for i in range(n, -1, -1):
        #print(i)
        new_string += texto[i]
    return new_string

def rot13(texto):
    old_string = list(texto)
    new_string = ""
    for i in old_string:
        new_string += rot.rotate(i,13)
    return new_string