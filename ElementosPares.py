def ElementosPares(Lista=[1,2,4,6,3,5,7]):
    ContadorPares=0
    for i in range(0,len(Lista)):
        if Lista[i] % 2 == 0:
            ContadorPares = ContadorPares + 1
 
    return ContadorPares

