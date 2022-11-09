def factorial(numero):
  return 1 if (numero == 1 or numero == 0) else numero * factorial(numero - 1)