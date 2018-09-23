def ListaPrimos(NumerosDeseados=50):
    ListaPrimos=[]
    for i in range(1,NumerosDeseados):
	if i % 2 != 0:
		ListaPrimos.append(i) 
    return ListaPrimos

