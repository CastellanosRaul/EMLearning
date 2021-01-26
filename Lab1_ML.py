print('______________________________________________')

print('Triangulo Invertido')

def i_triangle(n):
    return '\n'.join([
        '{}{}'.format(
            '  ' * (n-i),
            '* ' * (2*i-1)
        )
        
        for i in range(n,0,-1)
    ])

print(i_triangle(4))
print('')
print(i_triangle(5))
print('')
print(i_triangle(6))
print('')

print('______________________________________________')

print('Ecuacion de recurrencia' )

def ecua_rec(n, m):
    if n > m and m > 0:
        return ((n-1)/m) + ((n-1)/(m-1))
    elif m == n:
        return 1
    elif m == 0:
        return 1
    
print(ecua_rec(50, 35))
print('')
print(ecua_rec(100, 85))
print('')

print('prueba con resultado de 1')

print('')
print(ecua_rec(50, 0))
print('')
print(ecua_rec(100, 100))

print('______________________________________________')

print('Rombos con asterisco')

def rombo(a):
    linea = a/2 + 0.5 #redondeo a la mitad + 1 (linea mas larga del rombo)
    b = round(linea)
    for i in range(b):
        print(' ' * (b-1-i) + '* ' * (i+1))
    linea2 = a/2 - 0.5 #redondeo a la mitad + 1 (linea en decrecimiento)
    c = round(linea2)
    for i in range(c,0,-1):
        print(' ' * (b-i) + '* ' * i)

rombo(7)
print('')
rombo(9)
print('')
rombo(11)
print('')

print('______________________________________________')

print('Numeros primos menores a 100,000 en un segundo')
# Intento 

# lista = []
# def pares (x,y):
#     for num in range(x, y + 1):
#         if num > 1:
#             for i in range(2, num):
#                 if (num % i) == 0:
#                     break
#             else: lista.append(num)
#     print(lista)

# from time import process_time
# start = process_time()
# pares(0,100000)            
# stop = process_time()
# print(stop-start)
