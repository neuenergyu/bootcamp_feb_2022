


suma = 1
termino = 1
for i in range(1,500 + 1):
    
    suma = suma + 4 * termino + (10) * 2 * i
    termino = termino + 4 * 2 * i
    
    print('para lado {}, la suma va en {}'.format(i*2 + 1, suma))
    # print(termino)
 
print('\n')
print('para lado {}, la suma dio en {}'.format(i*2 + 1, suma))