#lista comprensiva
a = [2*x for x in range(1,10+1)]
print(a)

a = [(2*x)+1 for x in range (0,5)]
print (a)

a = [n for n in range(1,10,2)]
print(a)

#si es muktiplo de 3 tiene que salir 0 
print([0 if x % 3 == 0 else x for x in range(1, 10, 2)])