import re

def separar (valores):
    if valores == None:
        return []
    else:
        bloque = re.split(r'(\+|\-|\*|\/)', valores)
        return bloque

def numeros(bloque):
    segmento= []
    for bloques in bloque:
        if bloques.isnumeric():
            segmento.append(float(bloques))
        else:
            segmento.append(bloques)
    return segmento


def operar(bloque):
    if not isinstance(bloque, list):
        raise TypeError("El argumento debe ser una lista")

    i = 0
    while i < len (bloque):
        if bloque[i] == "*":
            if isinstance(bloque[i-1],(int,float)) and isinstance(bloque[i+1],(int,float)):
                resultado = bloque[i - 1] * bloque[i + 1]
                bloque[i - 1:i + 2] = [resultado]
                i -= 1
                print(resultado)
        elif bloque[i] == "/":
             if isinstance(bloque[i-1],(int,float)) and isinstance(bloque[i+1],(int,float)):
                resultado = bloque[i - 1] / bloque[i + 1]
                bloque[i - 1:i + 2] = [resultado]
                i -= 1
                print(resultado)
        elif bloque[i] == "+":
            if isinstance(bloque[i-1],(int,float)) and isinstance(bloque[i+1],(int,float)):
                resultado = bloque[i - 1] + bloque[i + 1]
                bloque[i - 1:i + 2] = [resultado]
                i -= 1
                print(resultado)
        elif bloque[i] == "-":
             if isinstance(bloque[i-1],(int,float)) and isinstance(bloque[i+1],(int,float)):
                resultado = bloque[i - 1] - bloque[i + 1]
                bloque[i - 1:i + 2] = [resultado]
                i -= 1
                print(resultado)
        i += 1
    return bloque