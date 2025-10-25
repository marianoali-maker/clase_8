

while True:  # Alexis

    print(f"\n{'-'*40} La trifecta {'-'*40}")

    while True:

        num = (input(f"\nPor favor ingresa un número: "))
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

        # Calcula el factorial del número de letras de la palabra o frase
        num_word = len(word)

        if num_word % 2 == 0:  # Verifica el número
            par = "par"  # si es par

        else:  # tambien
            par = "impar"  # si es impar

        # Muestra el resultado en pantalla
        print(
            f"\nEl número factorial de la palabra es {num_word} y es un número *{par}*")

        print(f"\n{'-'*40} La trifecta {'-'*40}")  # nombre del programa
