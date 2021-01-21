#Triangulo Invertido

def i_triangle(n):
    return '\n'.join([
        '{}{}'.format(
            '*' * (n-1-i),
            '' * (2*i+1)
        )
        
        for i in range(n)
    ])

print(i_triangle(1))

print(i_triangle(2))

print(i_triangle(3))

print(i_triangle(4))

print(i_triangle(5))

print(i_triangle(6))
