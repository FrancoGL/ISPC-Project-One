# Ejercicio 8
historial4 = (7510, 7960, 76180, 800, 4100)
nombre_mascota = "Olivia"

def valor_minimo(historial, mascota):
  historial_ordenado = tuple(sorted(historial))
  print(mascota + ",", "Valor mínimo gastado: " + str(historial_ordenado[0]))
  
valor_minimo(historial4, nombre_mascota)