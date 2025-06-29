#ejercicio 1

def operar(a, b, operador):
    try:
        if operador == '+':
            return a + b
        elif operador == '-':
            return a - b
        elif operador == '*':
            return a * b
        elif operador == '/':
            if b == 0:
                raise ZeroDivisionError("No se puede dividir por cero.")
            return a / b
        else:
            raise ValueError("Operador no válido. Usa '+', '-', '*', o '/'.")
    except Exception as e:
        return f"Error: {e}"

print(operar(1, 2, '+'))  
print(operar(5, 0, '/'))  

#ejercicio2

def es_palindromo(palabra):
    if not isinstance(palabra, str):
        raise TypeError("Se esperaba una cadena de texto.")
    if len(palabra) == 0:
        raise ValueError("La palabra no puede estar vacía.")
    
    n = len(palabra)
    for i in range(n // 2):
        if palabra[i] != palabra[n - 1 - i]:
            return False
    return True

# Ejemplo
print(es_palindromo("oso"))      # True
print(es_palindromo("python"))   # False

#ejercicio3

def es_primo(n):
    if not isinstance(n, int):
        raise TypeError("Se esperaba un número entero.")
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filtrar_primos(lista):
    if not isinstance(lista, list):
        raise TypeError("Se esperaba una lista.")
    
    return [num for num in lista if isinstance(num, int) and es_primo(num)]

# Ejemplo
print(filtrar_primos([2, 4, 7, 8, 11]))  # [2, 7, 11]


#ejercicio4

def mayor_suma_consecutivos(lista):
    if not isinstance(lista, list):
        raise TypeError("Se esperaba una lista.")
    if len(lista) < 2:
        raise ValueError("La lista debe contener al menos dos elementos.")
    for num in lista:
        if not isinstance(num, (int, float)):
            raise ValueError("Todos los elementos deben ser números.")
    
    max_suma = lista[0] + lista[1]
    for i in range(1, len(lista) - 1):
        suma = lista[i] + lista[i + 1]
        if suma > max_suma:
            max_suma = suma
    return max_suma

# Ejemplo
print(mayor_suma_consecutivos([1, 5, 3, 2]))  # 8


#ejercicio5

def mismos_caracteres(palabra1, palabra2):
    return sorted(palabra1) == sorted(palabra2)

def filtrar_anagramas(lista):
    if not isinstance(lista, list):
        raise TypeError("Se esperaba una lista.")
    if not all(isinstance(p, str) for p in lista):
        raise ValueError("Todos los elementos deben ser cadenas.")
    
    resultado = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if mismos_caracteres(lista[i], lista[j]):
                if lista[i] not in resultado:
                    resultado.append(lista[i])
                if lista[j] not in resultado:
                    resultado.append(lista[j])
    return resultado

# Ejemplo
print(filtrar_anagramas(["amor", "roma", "perro"]))  # ['amor', 'roma']
