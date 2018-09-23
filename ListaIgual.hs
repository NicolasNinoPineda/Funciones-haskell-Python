igualLista:: Eq a => [a]->[a]->Bool
igualLista l1 l2 = l1 == l2

main = print (igualLista ["Hola","Mundo"] ["Mundo","Hola"])
