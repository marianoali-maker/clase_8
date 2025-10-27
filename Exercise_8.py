while True:  # Alexis

    print(f"\n{'-'*40} La trifecta {'-'*40}")

    num = input("\nPor favor ingresa un número: ")

    if not num.isdigit():
        print("\n!!Dato Inválido, por favor vuelva a ingresar un valor válido!!")
        continue

    num = int(num)  

    if num == 0:
        print("\nSe ingresó 0. Fin del programa.")
        break

    # Ingresa una palabra o frase
    word = input("\nPor favor ingrese una palabra o frase: ")

    # Calcula cuántos caracteres tiene (incluyendo espacios)
    num_word = len(word)

    print(f"\nHola, tu frase tiene: * {num_word} * letras")

    # Función factorial
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    # Calcula el factorial del largo de la palabra/frase
    resultado = factorial(num_word)

    print(f"\nEl factorial de '{word}' es: {resultado}")

    if resultado % 2 == 0:
        print("\n El resultado es Par.")
    else:
        print("\nEl resultado es Impar.")

    print(f"\n{'-'*40} La trifecta {'-'*40}")
