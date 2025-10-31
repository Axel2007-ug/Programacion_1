# Mini Calculadora Interactiva

while True:
    print("\n--- MINI CALCULADORA INTERACTIVA ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Selecciona una opción (1-5): ")

    if opcion == "5":
        print("¡Gracias por usar la calculadora! 👋")
        break  # Sale del bucle while

    if opcion in ["1", "2", "3", "4"]:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if opcion == "1":
            resultado = num1 + num2
            print(f"Resultado: {num1} + {num2} = {resultado}")
        elif opcion == "2":
            resultado = num1 - num2
            print(f"Resultado: {num1} - {num2} = {resultado}")
        elif opcion == "3":
            resultado = num1 * num2
            print(f"Resultado: {num1} × {num2} = {resultado}")
        elif opcion == "4":
            if num2 != 0:
                resultado = num1 / num2
                print(f"Resultado: {num1} ÷ {num2} = {resultado}")
            else:
                print("Error: No se puede dividir entre cero.")
    else:
        print("Opción no válida. Intenta nuevamente.")