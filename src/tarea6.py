def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Ejemplo de uso para generar los primeros 10 números de la secuencia
n = 10
resultado = fibonacci(n)
print(f"Secuencia de Fibonacci de los primeros {n} números: {resultado}")
