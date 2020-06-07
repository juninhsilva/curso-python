x = int(input('Digite um numero: '))
div = 0
for y in range(1, x + 1):
    if x % y == 0:
        print(y)
        div += 1
if div > 2:
    print('Numero nao eh primo')
else:
    print('Numero eh primo')

a = 0
while a <= 10:
    print(a)
    a += 1