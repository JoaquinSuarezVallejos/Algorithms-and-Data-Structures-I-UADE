# Algoritmos y Estructuras de Datos I: Clase 1 - Repaso Inicial

# Ejercicio 1: Ingrese su número de documento o un número de 8 dígitos. Informar cuántos dígitos primos tiene el número ingresado.
def Ejercicio1():
    num = int(input("Ingresá tu DNI o un número de 8 dígitos: "))
    
    def informar_primos(num):
        contador_primos = 0
        for i in str(num):
            if i in "2357":
                contador_primos += 1
        return contador_primos

    print(f"El número {num} tiene {informar_primos(num)} números primos.")
    
    
# Ejercicio 2: Ingresar la longitud de una lista validando que esté entre 15 y 20. Cargar la lista con valores random entre 100 y 500. Mostrar la lista obtenida.
def Ejercicio2():
    longitud = int(input("Ingresá la longitud de una lista (15 - 20): "))
    
    while longitud < 15 or longitud > 20:
        longitud = int(input("Por favor, ingresá una longitud válida (15 - 20): "))
        
    def cargar_lista(longitud):
        from random import randint
        lista = []
        
        for i in range(longitud):
            lista.append(randint(100, 500))
            
        lista.sort()
        return lista
    
    print("La lista obtenida es: ", cargar_lista(longitud))
    
    
# Ejercicio 3: Definir dos listas A y B ordenadas de forma ascendente. Obtener una tercer lista C con los valores de las dos listas anteriores, 
# pero que C vaya quedando ordenada a medida que se va generando.
def Ejercicio3():
    listaA = [1, 3, 5, 7, 9, 11, 13, 19, 41]
    listaB = [2, 4, 6, 8, 10, 20, 21, 37, 50]
    listaC = []
    
    def ordenar_listaC(listaA, listaB):
        i = 0
        j = 0
        
        while i < len(listaA) and j < len(listaB):
            if listaA[i] < listaB[j]:
                listaC.append(listaA[i])
                i += 1
            else:
                listaC.append(listaB[j])
                j += 1
                
        while i < len(listaA):
            listaC.append(listaA[i])
            i += 1
            
        while j < len(listaB):
            listaC.append(listaB[j])
            j += 1
            
        return listaC
    
    print("La lista C ordenada es: ", ordenar_listaC(listaA, listaB))
    
    
# Ejercicio 4: Búsqueda Binaria
def Ejercicio4():
    lista = [2, 8, 10, 15, 20, 38]
    
    num = int(input("Ingrese un número para buscar en una lista misteriosa: "))

    min = 0
    max = len(lista)-1
    posicion = -1
    
    while min <= max and posicion == -1:
        medio = (min + max) // 2
        
        if num == lista[medio]:
            posicion = medio
        
        elif num < lista[medio]:
            max = medio - 1
        
        else:
            min = medio + 1
    
    if posicion == -1:
        print(f"El número {num} no se encuentra en la lista.")
    else:
        print(f"El número {num} se encuentra en la posición {posicion} de la lista.")
    
        
############################################################################################################

exit_check = False

while exit_check == False:
    ejercicioSeleccionado = int(input("\nIngresá el número del ejercicio que querés ejecutar (del 1 al 4) o '0' para salir del programa: "))
    if ejercicioSeleccionado == 1:
        Ejercicio1()
    elif ejercicioSeleccionado == 2:
        Ejercicio2()
    elif ejercicioSeleccionado == 3:
        Ejercicio3()
    elif ejercicioSeleccionado == 4:
        Ejercicio4()
    elif ejercicioSeleccionado == 0:
        exit_check = True
        print("Programa finalizado. ¡Hasta luego!")
    else:
        print("El número ingresado no corresponde a ningún ejercicio. Por favor, ingresá un número del 1 al 4 o '0' para salir del programa: ")