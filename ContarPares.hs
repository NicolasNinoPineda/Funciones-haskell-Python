contarpares::[Int]->Int
contarpares []=0
contarpares lista= length [x | x <- lista, mod x 2 ==0]

main = print (contarpares [2,34,56,22,15,9,76])
