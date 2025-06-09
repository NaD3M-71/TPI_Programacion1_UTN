"""El programa fue realizado por ambos, y cabe aclarar que ambos tenemos conocimiento previo en programacion"""
"""Mariano Rossi trabaja como Desarrollador DevOps para una empresa Multinacional, y Giuliano Scaglioni trabaja como Programador para un ente gubernamental y tambien hace trabajos de desarrollo FullStack de forma independiente"""
"""Hacemos esta aclaración en el caso de encontrarse en el codigo temas ( por ejemplo: manejo de errores) aún no presentados en la cursada"""
#  Proyecto: Comparación de Algoritmos de Ordenamiento - Bubble Sort y Cocktail Sort
##  Descripción

Este proyecto implementa y compara dos algoritmos de ordenamiento clásicos: **Bubble Sort** (ordenamiento descendente) y **Cocktail Sort** (ordenamiento bidireccional ascendente). Está desarrollado en Python con un enfoque modular, permitiendo al usuario seleccionar el tipo y tamaño del array a ordenar, visualizar los resultados y medir el rendimiento de cada algoritmo.

---

##  Estructura del Proyecto

- `bubblesort.py`: Contiene la lógica del algoritmo Bubble Sort.
- `cocktail.py`: Implementa el algoritmo Cocktail Sort.
- `pruebas.py`: Genera diferentes arrays de prueba (predefinidos o personalizados).
- `index.py`: Interfaz principal del programa (menú, ejecución, comparación).

---

##  Cómo Ejecutarlo

1. Asegúrate de tener Python 3.10 o superior instalado.
2. Ejecuta el archivo principal:

```bash
python index.py
```

3. Sigue las instrucciones en consola para:
   - Ordenar un array con Bubble Sort.
   - Ordenar un array con Cocktail Sort.
   - Comparar ambos algoritmos.
   - Salir del programa.

---

##  Casos de prueba

El programa permite elegir entre:
- Array pequeño: 7 elementos predefinidos.
- Array mediano: 20 elementos aleatorios.
- Array grande: 100 elementos aleatorios.
- Array muy grande: 1000 elementos aleatorios.
- Array personalizado: definido por el usuario (ideal para DNIs u otros datos reales).

---

##  Evaluación de rendimiento

Se midió el tiempo de ejecución con `time.time()` y se obtuvieron resultados como:

| Algoritmo         | Pasadas | Tiempo (1000 elementos) |
|-------------------|---------|--------------------------|
| Bubble Sort       | 990     | 48.697 ms               |
| Cocktail Sort     | 260     | 66.286 ms               |

---

##  Autores

- Giuliano Scaglioni
- Mariano Rossi

**Comisión:** 21  
**Carrera:** Tecnicatura Universitaria en Programación a distancia.
**Institución:** Universidad Tecnológica Nacional (UTN).

---

##  Fuentes Consultadas

- Skiena, S. (2008). *The Algorithm Design Manual*.
- Heineman, G. et al. (2008). *Algorithms in a Nutshell*.
- Rod Stephens. *Essential Algorithms*.
- Donald Knuth. *The Art of Computer Programming*.
- UTN SIED: [https://tup.sied.utn.edu.ar](https://tup.sied.utn.edu.ar)
- ResearchGate: Imagen de cocktail sort.

---

##  Posibles mejoras

- Incorporar algoritmos adicionales (Quick Sort, Merge Sort).
- Agregar visualización gráfica del proceso.
- Interfaz gráfica para mayor accesibilidad.
- Exportar resultados a archivo.
