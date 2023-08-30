"""
    Creado por Yadir Vega Espinoza 
    Curso: Programación lineal
    Objetivo: Repaso básico de python

    Reto 1:

            Deberán cargar el paquete numpy como np.
            Construir una función llamada OperaMatriz(A,B,txt) donde A, B son matrices y txt es una de las siguientes 
            frases: "suma","resta","multiplica".
            La función deberá retornar la suma A+B en caso que txt="suma", A-B si txt="resta" y A*B si txt="multiplica". 
            Se debe validar que la operación sea válida según las dimensiones de las matrices.
            No programen las operaciones, sino que usen el paquete numpy.

    Fecha: 2023-08-29
"""

# paquete solicitado
import numpy as np 

# valida segun la operacion a realizar
def Valida_Operaciones(A, B, txt):
    txt = txt.lower()
    if txt not in ('suma', 'resta', 'multiplica'):
        return 'Operación no permitida, ingrese suma, resta o multiplica'
    else:
        if txt in ('suma', 'resta'):
            if A.shape != B.shape:
                return 'Las matrices ingresadas A y B deben tener la misma dimensión para realizar la operación'
            else: 
                return True
        elif txt == 'multiplicacion':
            if A.shape[1] != B.shape[0]:
                print(A.shape[1],B.shape[0])
                return 'El número de columnas de A debe coincidir con el número de filas de B para poder realizar la operación'
            else:
                return True
            
# funcion solictada
def OperaMatriz(A, B, txt):
    validacion_dimensiones = Valida_Operaciones(A, B, txt)
    txt = txt.lower()
    if validacion_dimensiones:
        if txt == 'suma':
            return A+B
        elif txt == 'resta':
            return A-B
        elif txt == 'multiplica':
            return A*B
    else:
        return validacion_dimensiones

# ejemplo de uso
def Prueba_Reto():
    # matrices de prueba
    A = np.array([[1, 2], [3,5]])
    B = np.array([[1, 2],[3,5]])
    # operacion
    txt = 'RESTA'
    # imprimimos resultado o error
    print(OperaMatriz(A, B, txt))

# Main de la app
if __name__ == "__main__":
    Prueba_Reto()