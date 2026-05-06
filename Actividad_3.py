# Actividad 3: Clasificador de IMC

# 1. Solicitar datos al usuario
peso_str = input("Ingrese su peso en kg: ")
estatura_str = input("Ingrese su estatura en metros (ejemplo: 1.70): ")

# Validación de que no falten datos
if not peso_str.strip() or not estatura_str.strip():
    print("Error: Falta ingresar el peso o la estatura.")
else:
    peso = float(peso_str)
    estatura = float(estatura_str)

    # 5. Bonus: Validar valores positivos
    if peso <= 0 or estatura <= 0:
        print("Error: El peso y la estatura deben ser valores mayores a cero.")
    else:
        # 2. Calcular el IMC
        # Formula: peso / (estatura ** 2)
        imc = peso / (estatura ** 2)
        imc_redondeado = round(imc, 2)

        # 3. Clasificar el resultado con if / elif / else
        if imc < 18.5:
            clasificacion = "Bajo peso"
        elif 18.5 <= imc <= 24.9:
            clasificacion = "Normal"
        elif 25 <= imc <= 29.9:
            clasificacion = "Sobrepeso"
        else:
            clasificacion = "Obesidad"

        # 4. Imprimir resultados
        print("-" * 30)
        print(f"Tu IMC es: {imc_redondeado}")
        print(f"Clasificación: {clasificacion}")
        print("-" * 30)