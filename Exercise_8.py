while True:  # Alexis

    print(f"\n{'-'*40} La trifecta {'-'*40}")

    while True:

        num = (input("\nPor favor ingresa un número: "))
        if num.isdigit():
            num = int(num)

            if num == 0:
                print("\nSe ingresó 0. Fin del programa.")
                break

        else:
            print("\n!!Dato Inválido, por favor vuelva a ingresar un valor válido!!")
            break

        # Ingesa una palabra o frase
        word = input("\nPor favor ingrese una palabra o frase: ")
        # Muestra la cantidad de letras que tiene la palabra o frase
        print(f"\nHola tu frase tiene: * {len(word)} * letras")

    def factorial(n):
        if (n == 0):
            return 1
        else:
            return n * factorial(n-1)

    resultado = factorial(num)
    print("El factorial de: " + str(word) + ": es: " + str(resultado))

    if resultado % 2 == 0:
        print("El resultado es par.")
    else:
        print("El resultado es impar.")

    print(f"\n{'-'*40} La trifecta {'-'*40}")  # nombre del programa
