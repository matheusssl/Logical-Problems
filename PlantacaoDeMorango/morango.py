c1 = int(input('Comprimento do 1o local em metros: '))
l1 = int(input('Largura do 1o local em metros: '))

c2 = int(input('Comprimento do 2o local em metros: '))
l2 = int(input('Largura do 2o local em metros: '))

a1 = c1 * l1
a2 = c2 * l2

if a1 > a2:
    print(f'A área é, {a1}m², portanto, o local 1 é o mais adequado')

elif a1 == a2:
    print('Ambas as áreas são adequadas')

else:
    print(f'A área é {a2}m², portanto, o local 2 é o mais adequado')
