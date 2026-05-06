def pedir_nota(mensaje):
    while True:
        entrada = input(mensaje)

        if not entrada.strip():
            print("Error: Falta una nota. Por favor, ingresa un valor.")
            continue
        try:
            nota = float(entrada)
            if nota > 5.0:
                print("Error: La nota no puede ser mayor a 5.0. Intenta de nuevo.")
            elif nota < 0:
                print("Error: La nota no puede ser negativa.")
            else:
                return nota
        except ValueError:
            print("Error: Debes ingresar un número válido.")

# Pedir las notas usando la función de validación
nota1 = pedir_nota("Ingrese la primera nota: ")
nota2 = pedir_nota("Ingrese la segunda nota: ")
nota3 = pedir_nota("Ingrese la tercera nota: ")

# Cálculo del promedio
promedio = (nota1 + nota2 + nota3) / 3
promedio_redondeado = round(promedio, 2)

# Cálculo de puntos faltantes para la nota máxima
puntos_faltantes = round(5.0 - promedio, 2)

# Resultados con formato legible
print("-" * 30)
print(f"Promedio final: {promedio_redondeado}")
print(f"Puntos para el 5.0: {puntos_faltantes}")

if promedio >= 3.0:
    print("Resultado: Aprobado")
else:
    print("Resultado: Reprobado")
print("-" * 30)