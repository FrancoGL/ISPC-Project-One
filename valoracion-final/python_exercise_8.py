# Ejercicio 8
historial4 = (7510, 7960, 76180, 800, 4100)
nombre_mascota = "Olivia"


def valor_minimo(historial):
    historial_ordenado = tuple(sorted(historial))
    return historial_ordenado


historial_ordenado = valor_minimo(historial4)

print(nombre_mascota + ",", "Valor mínimo gastado: " +
      str(historial_ordenado[0]))
