def cantidad_segundos(h, m, s):
  hs = h * 60 * 60
  ms = m * 60
  total = hs + ms + s
  print("\nLa cantidad total de segundos es: ", total)


def segundos_a_segundos_minutos_y_horas(segundos):
  min = segundos // 60
  seg_resto = segundos % 60
  hor = min // 60
  min_resto = min % 60

  print("Detalle: ", hor, "hs,", min_resto, "ms,", seg_resto, "s")