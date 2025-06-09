import random

def generar_array_aleatorio(tamaño, minimo=0, maximo=1000):
    """
    Genera un array de números aleatorios
    
    Args:
        tamaño: cantidad de elementos
        minimo: valor mínimo (por defecto 0)
        maximo: valor máximo (por defecto 1000)
    
    Returns:
        Lista con números aleatorios
    """
    return [random.randint(minimo, maximo) for _ in range(tamaño)]

def obtener_arrays_prueba():
    """
    Retorna diccionario con diferentes arrays de prueba
    """
    arrays_prueba = {
        'pequeño': [64, 34, 25, 12, 22, 11, 90],
        'mediano': generar_array_aleatorio(20),
        'grande': generar_array_aleatorio(100),
        'muy_grande': generar_array_aleatorio(1000),
        
    }
    return arrays_prueba

def mostrar_opciones():
    """Muestra las opciones de arrays disponibles"""
    print("\n=== ARRAYS DE PRUEBA DISPONIBLES ===")
    print("1. pequeño - Array de 7 elementos predefinidos")
    print("2. mediano - 20 números aleatorios (0-1000)")
    print("3. grande - 100 números aleatorios (0-1000)")
    print("4. muy_grande - 1000 números aleatorios (0-1000)")
    print("5. personalizado - Ordenamiento por DNIs")

def crear_array_personalizado():
    """Permite al usuario crear un array personalizado"""
    try:
        tamaño = int(input("Ingresa el tamaño del array: "))
        minimo = int(input("Valor mínimo (por defecto 0): ") or "0")
        maximo = int(input("Valor máximo (por defecto 1000): ") or "1000")
        return generar_array_aleatorio(tamaño, minimo, maximo)
    except ValueError:
        print("Error: Ingresa solo números enteros")
        return None