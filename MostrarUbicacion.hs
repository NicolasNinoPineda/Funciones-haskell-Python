mostrar_ubicacion::Ord a=>[a]->Int->a
mostrar_ubicacion l n = l!!n

main = print (mostrar_ubicacion [15,20,35,21] 3)
