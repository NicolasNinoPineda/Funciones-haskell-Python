def CuadradosLIsta(Lista=[1,2,4,6,3,5,7]):
    ListaCuadrados=[]
    for i in range(0,len(Lista)):
        CuadradoNumero = Lista[i] * Lista [i]
	ListaCuadrados.append(CuadradoNumero) 
    return ListaCuadrados
