import numpy as np

# Ejercicio 2-a
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
    - Aproximación del mínimo encontrada (numpy array).
    """
    x = x0
    for i in range(int(maxit)):
        gradiente = grad_f(x)
        norma_gradiente = np.linalg.norm(gradiente, ord=2)  # Norma 2 del gradiente
        
        # Verificar si la norma del gradiente es menor que la tolerancia
        if norma_gradiente < tol:
            print(f"Convergencia alcanzada en la iteración {i}.")
            return x
        
        # Actualizar el punto según la regla de descenso de gradiente
        x = x - gamma * gradiente
    
    print(f"Se alcanzó el número máximo de iteraciones ({maxit})")
    return x

# Ejercicio 2-c-1
def grad_f(x):
    """
    Calcula el gradiente de la función g(x, y) = x^2 + y^3 + 3xy + 1.

    Parámetros:
    - x: Vector de dos componentes [x, y] (numpy array).

    Retorna:
    - Gradiente en el punto (numpy array).
    """
    grad_x = 2 * x[0] + 3 * x[1] # Derivada parcial respecto a x
    grad_y = 3 * x[1]**2 + 3 * x[0] # Derivada parcial respecto a y
    return np.array([grad_x, grad_y])

# Parámetros de entrada
x0 = np.array([-1.0, 1.0])  # Punto inicial
gamma = 0.01  # Tasa de aprendizaje
tol = 1e-12  # Tolerancia
maxit = 1e5  # Máximo de iteraciones

# Llamada a la función
resultado = gradiente_descendente(grad_f, x0, gamma, tol, maxit)
print(f"Resultado con x0 = (-1,1): {resultado}")


# Ejercicio 2-c-2
x0 = np.array([0.0, 0.0])  # Nuevo punto inicial

# Llamada a la función
resultado2 = gradiente_descendente(grad_f, x0, gamma, tol, maxit)
print(f"Resultado con x0 = (0,0): {resultado2}")

# Ejercicio 2-c-3
"""
Análisis de los resultados:
Buscamos los puntos críticos donde ∇g(x,y)=0
2x + 3y = 0
3y^2 + 3x = 0
 
De la primera ecuación:
x = -3/2y

Sustituimos en la segunda:
3y^2 + 3(-3/2y) = 0  => 3y^2 - 9/2y = 0
y(3y - 9/2) = 0 => y = 0 o y = 3/2

Si y = 0, entonces x = 0
Si y = 3/2, entonces x = -3/2(3/2) = -9/4

Puntos críticos: (0,0) y (-9/4, 3/2)

Comportamiento inicial:
1. x0 = (0,0): El punto inicial es un punto crítico, por lo que el algoritmo no se moverá.
2. x0 = (-1,1): Se aproxima al punto crítico (-9/4, 3/2) desde la dirección opuesta al gradiente.

Análisis:
El punto inicial (0,0) es un punto crítico por lo que no es deseable. El descenso desde otros puntos busca el mínimo local.

Conclusiones:
1. Desde el punto (-1,1) se alcanza el mínimo local (-9/4, 3/2).
2. Desde el punto (0,0) no se alcanza porque el gradiente inicial es cero.
3. El análisis confirma que (0,0) es un punto crítico no deseable y explica la convergencia hacia el mínimo local (-9/4, 3/2) desde (-1,1).
"""