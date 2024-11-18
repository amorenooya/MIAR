import numpy as np

def gradiente_descendente(grad_f, x0, gamma, tol, maxit):
    """
    Implementa el método de descenso de gradiente para minimizar una función.

    Parámetros:
    - grad_f: Función que calcula el gradiente de f en un punto x (vector).
    - x0: Vector inicial (numpy array) con n componentes.
    - gamma: Tasa de aprendizaje (float).
    - tol: Tolerancia para detener el algoritmo (float).
    - maxit: Número máximo de iteraciones (int).

    Retorna:
    - x: Aproximación del mínimo encontrada (numpy array).
    - iteraciones: Número de iteraciones realizadas.
    """
    x = x0
    for i in range(maxit):
        gradiente = grad_f(x)
        norma_gradiente = np.linalg.norm(gradiente, ord=2)  # Norma 2 del gradiente
        
        # Verificar si la norma del gradiente es menor que la tolerancia
        if norma_gradiente < tol:
            print(f"Convergencia alcanzada en la iteración {i}.")
            return x, i
        
        # Actualizar el punto según la regla de descenso de gradiente
        x = x - gamma * gradiente
    
    print("Se alcanzó el número máximo de iteraciones.")
    return x, maxit

# Ejemplo de uso
def grad_f(x):
    # Gradiente de la función f(x, y) = (x-2)^2 + (y+3)^2
    return np.array([2 * (x[0] - 2), 2 * (x[1] + 3)])

# Parámetros de entrada
x0 = np.array([0.0, 0.0])  # Punto inicial
gamma = 0.1  # Tasa de aprendizaje
tol = 1e-6  # Tolerancia
maxit = 1000  # Máximo de iteraciones

# Llamada a la función
resultado, iteraciones = gradiente_descendente(grad_f, x0, gamma, tol, maxit)
print(f"Resultado: {resultado}")
print(f"Iteraciones: {iteraciones}")
