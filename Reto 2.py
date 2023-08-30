"""
    Creado por Yadir Vega Espinoza 
    Curso: Programación lineal
    Objetivo: Repaso básico de python

    Reto 1:
        Construya una función llamada matriz2Latex(A), que reciba una matriz A y retorne el código LaTeX de una tabla como en el siguiente ejemplo:
        A=np.array([[1, 2, 3],
                                [4, 5, 6],
                                [7, 8, 9],
                                [10, 11, 12]])
        Al final se deberá retornar el código LaTeX para generar la tabla de la imagen.

    Fecha: 2023-08-29
"""
# para operar matrices
import numpy as np

# funcion solicitada
def matriz2Latex(A):
    # lista por compresion
    filas_latex = [" & ".join(map(str, row)) + " \\\\" for row in A]
    # Combinacion
    codigo_latex = "\\begin{bmatrix}\n" + "\n".join(filas_latex) + "\n\\end{bmatrix}"
    return codigo_latex

# ejemplo de uso
def Prueba_Reto():
# Ejemplo de uso
    A = np.array([[15, 52, 38],[4,10, 16],[71, 82, 39],[130, 131, 121]])
    tabla_latex = matriz2Latex(A)
    print(tabla_latex)

# Main de la app
if __name__ == "__main__":
    Prueba_Reto()





