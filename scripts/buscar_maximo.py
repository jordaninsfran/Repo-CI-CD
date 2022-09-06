def get_maximo(valores):
	maximo = valores[0]
	for i in range(valores):
		if(valores[i] > maximo):
			maximo = valores[i]
	return maximo
