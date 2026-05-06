# ejercicio creativo 

#enunciado 

# se hara una calculadora de divisas donde se pida primero 
# la obciones de entre 4 divisas las cuales son euro dolar 
# yenes o soles peruanos se le va a pedir cantidad de pesos 
# colombianos y se hara la convercion que solicito.

# 1. Mostrar opciones al usuario
print("Bienvenido a la calculadora de divisas")
print("Opciones disponibles:")
print("1. Euro (EUR)")
print("2. Dólar (USD)")
print("3. Yenes (JPY)")
print("4. Soles Peruanos (PEN)")

opcion = input("seleccione el numero de la divisa q desea convertir:")

if not opcion.strip():
    print("Error: No seleccionaste ninguna opción.")
else:
    # Pedir la cantidad de pesos colombianos
    cantidad_cop_str = input("Ingrese la cantidad de Pesos Colombianos (COP) Como por ejemplo 25000: ")

    if not cantidad_cop_str.strip():
        print("Error: Debes ingresar una cantidad de dinero.")
    else:
        cantidad_cop = float(cantidad_cop_str)
        if cantidad_cop <= 0:
            print("Error: La cantidad debe ser mayor a cero.")
        else:
            if opcion == "1":
                resultado = cantidad_cop * 0.00027 
                moneda = "Euros"
            elif opcion == "2":
                resultado = cantidad_cop * 0.00025 
                moneda = "Dolares"
            elif opcion == "3":
                resultado = cantidad_cop * 0.042   # Tasa COP a Yenes
                moneda = "Yenes"
            elif opcion == "4":
                resultado = cantidad_cop * 0.00094 # Tasa COP a Soles
                moneda = "Soles Peruanos"
            else:
                resultado = None
            if resultado is None:
                print("Esta opcion de divisa no es valida")
            else:
                print("-" * 20)
                print(f"Cantidad original: {cantidad_cop} COP")
                print(f"Conversión final: {round(resultado, 6)} {moneda}")
                print("-" * 20)