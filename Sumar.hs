sumar::[Int]->Int
sumar [ ] = 0
sumar (x:xs) = x + sumar(xs)

main =  print (sumar [5,4,7,8] )
