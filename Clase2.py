# Clase 2
import array

numbers = [5, 4, 9]
words = ["cow", "chicken", "cat"]
grades = array.array('l', [8, 7, 9])

print(type(numbers))
print(type(words))

numbers.append(100)
numbers.pop(1) # por posición, si no se le da un argumento elimina el último elemento
numbers.remove(5) # por elemento existente en la lista, sí o sí se le debe dar un argumento
numbers.insert(1, 10) # inserta el número 10 en la posición 1, dos argumentos
numbers.clear() # elimina todos los elementos de la lista
numbers.sort(reverse=True) # Ordena la lista de mayor a menor. Si se le da un argumento reverse = True, de menor a mayor.

cadena = "Juan"
for i in range(len(cadena)):
    print(cadena[i], end="")
    
for c in cadena:
    print(c)

# Strings
s = "Python"
s.capitalize() # Pone la primera letra en mayúscula
s.upper() # Pone todas las letras en mayúscula
s.lower() # Pone todas las letras en minúscula
s.isalpha() # Devuelve True si todos los caracteres son alfabéticos
s.isdigit() # Devuelve True si todos los caracteres son dígitos

