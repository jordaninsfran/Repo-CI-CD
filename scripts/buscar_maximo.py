def get_maximo(valores):
	maximo = valores[0]
	for i in valores:
		if(i > maximo):
			maximo = i
	return maximo
