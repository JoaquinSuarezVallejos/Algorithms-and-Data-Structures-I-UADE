# Clase 2
import array

numbers = [5, 2, 4, 9, 2]
words = ["cow", "chicken", "cat"]
grades = array.array('l', [8, 7, 9])

print(type(numbers))
print(type(words))

numbers.append(100)
numbers.pop(1) # por posición, si no se le da un argumento elimina el último elemento
numbers.remove(5) # por elemento existente en la lista, sí o sí se le debe dar un argumento
numbers.insert(1, 10) # inserta el número 10 en la posición 1, dos argumentos
numbers.clear() # elimina todos los elementos de la lista
numbers.sort() # Ordena la lista de mayor a menor. Si se le da un argumento reverse = True, de menor a mayor.
numbers.reverse() # Invierte el orden de los elementos de la lista
numbers.count(2) # Cuenta cuántas veces aparece un elemento en la lista

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

s.endswith("on") # Devuelve True si la cadena termina con "on"
s.find("th") # Devuelve la posición de la primera ocurrencia de "th", si no lo encuentra devuelve -1
s.index("th") # Devuelve la posición de la primera ocurrencia de "th", si no lo encuentra devuelve un error, se puede usar try except
", ".join(s) # Concatena los elementos de la lista con la cadena, se le debe dar un argumento, ej: ", ".join(["a", "b", "c"]) -> "a, b, c"
s.lstrip() # Elimina los espacios en blanco a la izquierda
s.rstrip() # Elimina los espacios en blanco a la derecha
