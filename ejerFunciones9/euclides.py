def mcd(num1, num2):
	resto = 0
	while(num2 > 0):
		resto = num2
		num2 = num1 % num2
		num1 = resto
	return num1