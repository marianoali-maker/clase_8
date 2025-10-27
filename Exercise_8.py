while True:  # Bucle principal para repetir el proceso.

    print(f"\n{'-'*40} La trifecta {'-'*40}") # Encabezado del programa

    num = input("\nPor favor ingresa un número: ") # Solicita un número al usuario

    if not num.isdigit(): # Verifica si la entrada es un número válido
        print("\n!!Dato Inválido, por favor vuelva a ingresar un valor válido!!") # Mensaje de error por dato inválido
        continue # Reinicia el bucle si la entrada no es válida

    num = int(num)  # Convierte la entrada a entero

    if num == 0: # Condición para salir del programa 
        print("\nSe ingresó 0. Fin del programa.") # Mensaje de salida
        break # Sale del bucle principal

    # Ingresa una palabra o frase
    word = input("\nPor favor ingrese una palabra o frase: ") # Solicita una palabra o frase al usuario

    # Calcula cuántos caracteres tiene (incluyendo espacios)
    num_word = len(word)

    print(f"\nHola, tu frase tiene: * {num_word} * letras") # Muestra el número de caracteres

    # Función factorial
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    # Calcula el factorial del largo de la palabra/frase
    resultado = factorial(num_word)

    print(f"\nEl factorial de '{word}' es: {resultado}") # Muestra el resultado del factorial

    if resultado % 2 == 0:
        print("\n El resultado es Par.") # Indica si el resultado es par o impar
    else:
        print("\nEl resultado es Impar.") # Indica si el resultado es par o impar

    print(f"\n{'-'*40} La trifecta {'-'*40}")
