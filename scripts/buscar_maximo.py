def get_maximo(valores):
	maximo = valores[0]
	for i in range(len(valores)):
		if(valores[i] > maximo):
			maximo = valores[i]
	return maximo
