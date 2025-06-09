def imprimir_array(vector):

    print("[", end="")
    for elemento in vector:
        print(f" {elemento} ", end="")
    print(" ]")

def ord_burbuja(vector):
    """
    Algoritmo Bubble Sort u Ordenamiento Burbuja
    """
    n = len(vector)
    i = 0
    cambio = True
    
    while i <= n - 1 and cambio:
        cambio = False
        for j in range(n - i - 1):
            if vector[j] < vector[j + 1]:  # Ordenamiento descendente
                # Intercambio
                vector[j], vector[j + 1] = vector[j + 1], vector[j]
                cambio = True
        
        i += 1
        # Mostrar el array después de cada pasada (solo primeros 20 elementos si es muy grande)
        if len(vector) <= 20:
            print(f"Pasada {i}: primeros 20 elementos:", vector[:20])
    
    print(f"Finalizo el ordenamiento luego de {i} pasadas")
