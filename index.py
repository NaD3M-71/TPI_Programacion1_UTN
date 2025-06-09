from bubblesort import ord_burbuja, imprimir_array as imprimir_bubble
from cocktail import ord_cocktail, imprimir_array as imprimir_cocktail
from pruebas import obtener_arrays_prueba, mostrar_opciones, crear_array_personalizado
import time

def mostrar_menu_principal():
    """Muestra el menú principal"""
    print("\n" + "="*50)
    print("    ALGORITMOS DE ORDENAMIENTO")
    print("="*50)
    print("1. Bubble Sort (Ordenamiento Descendente)")
    print("2. Cocktail Sort (Ordenamiento Ascendente)")
    print("3. Comparar ambos algoritmos")
    print("4. Salir")
    print("="*50)

def seleccionar_array():
    """Permite al usuario seleccionar un array de prueba"""
    mostrar_opciones()
    arrays = obtener_arrays_prueba()
    
    opciones = {
        '1': 'pequeño', '2': 'mediano', '3': 'grande', '4': 'muy_grande'
    }
    
    while True:
        opcion = input("\nSelecciona una opción (1-5): ")
        if opcion in opciones:
            nombre_array = opciones[opcion]
            return arrays[nombre_array], nombre_array
        elif opcion == '5':
            array_personalizado = crear_array_personalizado()
            if array_personalizado:
                return array_personalizado, 'personalizado'
        else:
            print("Opción inválida. Intenta de nuevo.")

def ejecutar_bubble_sort():
    """Ejecuta el algoritmo Bubble Sort"""
    print("\n=== BUBBLE SORT (Descendente) ===")
    array, nombre = seleccionar_array()
    
    print(f"\nArray original ({nombre}):")
    imprimir_bubble(array)
    
    print(f"\nOrdenando {len(array)} elementos con Bubble Sort...")

    
    tiempo_inicio_bubble = time.time()
    ord_burbuja(array)
    tiempo_fin_bubble = time.time()
    tiempo_bubble = tiempo_fin_bubble - tiempo_inicio_bubble
    
    print(f"\nArray final ordenado (descendente):")
    print(f"Tiempo de ordenamiento: {tiempo_bubble:.6f} segundos({tiempo_bubble*1000:.3f} mseg)")
    imprimir_bubble(array)

def ejecutar_cocktail_sort():
    """Ejecuta el algoritmo Cocktail Sort"""
    print("\n=== COCKTAIL SORT (Ascendente) ===")
    array, nombre = seleccionar_array()
    
    print(f"\nArray original ({nombre}):")
    imprimir_cocktail(array)
    
    print(f"\nOrdenando {len(array)} elementos con Cocktail Sort...")

    
    
    tiempo_cocktail_inicio = time.time()
    ord_cocktail(array)
    tiempo_cocktail_fin = time.time()
    tiempo_cocktail= tiempo_cocktail_fin - tiempo_cocktail_inicio
    
    print(f"Tiempo de ordenamiento: {tiempo_cocktail:.6f} segundos({tiempo_cocktail*1000:.3f} mseg)")
    print(f"\nArray final ordenado (ascendente):")
    imprimir_cocktail(array)

def comparar_algoritmos():
    """Compara ambos algoritmos con el mismo array"""
    print("\n=== COMPARACIÓN DE ALGORITMOS ===")
    array, nombre = seleccionar_array()
    
    print(f"\nArray original ({nombre}):")
    print("Elementos:", len(array))

    imprimir_bubble(array)

    # Bubble Sort
    print(f"\n--- BUBBLE SORT (Descendente) ---")
    array_bubble = list(array)
    
    tiempo_inicio_bubble = time.time()
    ord_burbuja(array_bubble)
    tiempo_fin_bubble = time.time()
    tiempo_bubble = tiempo_fin_bubble - tiempo_inicio_bubble
    
    print("Resultado Bubble Sort:")
    
    imprimir_bubble(array_bubble)

    
    # Cocktail Sort
    print(f"\n--- COCKTAIL SORT (Ascendente) ---")
    array_cocktail = list(array)

    
    tiempo_cocktail_inicio = time.time()
    ord_cocktail(array_cocktail)
    tiempo_cocktail_fin = time.time()
    tiempo_cocktail= tiempo_cocktail_fin - tiempo_cocktail_inicio
    print("Resultado Cocktail Sort:")
    imprimir_cocktail(array_cocktail)
    
    print(f"Tiempo de ordenamiento de algoritmo Bubble: {tiempo_bubble:.6f} segundos({tiempo_bubble*1000:.3f} mseg)")
    print(f"Tiempo de ordenamiento de algoritmo Cocktail: {tiempo_cocktail:.6f} segundos({tiempo_cocktail*1000:.3f} mseg)")



"""Función principal"""
print("¡Bienvenido al programa de algoritmos de ordenamiento!")
opcion=0
while opcion!=4:
    mostrar_menu_principal()
    opcion = input("Selecciona una opción: ")
    
    if opcion == '1':
        ejecutar_bubble_sort()
    elif opcion == '2':
        ejecutar_cocktail_sort()
    elif opcion == '3':
        comparar_algoritmos()
    elif opcion == '4':
        print("\n¡Gracias por usar el programa!")
        break
    else:
        print("Opción inválida. Intenta de nuevo.")
    
    input("\nPresiona Enter para continuar...")

