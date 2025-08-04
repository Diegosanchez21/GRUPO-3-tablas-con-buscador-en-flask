import random

def generar_lista_aleatoria(n=10, min_val=1, max_val=100):
    return sorted(random.sample(range(min_val, max_val), n))

def busqueda_secuencial(lista, buscado):
    estados = ['no'] * len(lista)
    resultado = None
    for idx, val in enumerate(lista):
        estados[idx] = 'revisado'
        if val == buscado:
            estados[idx] = 'encontrado'
            resultado = idx
            break
    if resultado is None:
        return -1, estados
    else:
        return resultado, estados

def busqueda_binaria(lista, buscado):
    izquierda, derecha = 0, len(lista) - 1
    pasos = ['no'] * len(lista)
    resultado = None
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        pasos[medio] = 'revisado'
        if lista[medio] == buscado:
            pasos[medio] = 'encontrado'
            resultado = medio
            break
        elif lista[medio] < buscado:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    if resultado is None:
        return -1, pasos
    else:
        return resultado, pasos