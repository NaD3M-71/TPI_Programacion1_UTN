def imprimir_array(vector):
    print("[", end="")
    for elemento in vector:
        print(f" {elemento} ", end="")
    print(" ]")

def ord_cocktail(vector):
    """
    Algoritmo Cocktail Sort (Shaker Sort)
    Ordena el array de forma ascendente
    """
    n = len(vector)
    izq = 0
    der = n - 2
    cambios = True
    
    while izq < der and cambios:
        cambios = False
        
        # Pasada de izquierda a derecha
        for i in range(izq, der + 1):
            if vector[i] > vector[i + 1]:
                # Intercambio
                vector[i], vector[i + 1] = vector[i + 1], vector[i]
                cambios = True
        
        izq += 1
        
        # Pasada de derecha a izquierda
        for i in range(der, izq - 1, -1):
            if vector[i] < vector[i - 1]:
                # Intercambio
                vector[i], vector[i - 1] = vector[i - 1], vector[i]
                cambios = True
        
        der -= 1
    print(f"Finalizo el ordenamiento luego de {izq} pasadas")
    print()  # Nueva línea al final