lista_inteiros = [1,2,3,4,5]
lista_string = ['cachorro', 'gato', 'elefante']
print(lista_inteiros)
print(lista_string)

lista_pares = []

for x in range(10000):
    if x % 2 == 0:
        lista_pares.append(x);

lista_impares = []

for x in range(10000):
    if x % 2 != 0:
        lista_impares.append(x);

print(lista_pares)
print(sum(lista_pares))
print(max(lista_pares))
print(min(lista_pares))
print(sum(lista_pares) / len(lista_pares))

print(lista_impares)
print(sum(lista_impares))
print(max(lista_impares))
print(min(lista_impares))
print(sum(lista_impares) / len(lista_impares))

lista_inteiros.pop()
print(lista_inteiros)

print(lista_string.sort())
print(lista_string)

print(lista_string.reverse())
print(lista_string)

lista_string.remove('elefante')
print(lista_string)

tupla = (1, 3, 5, 7)
print(tupla)
print(tupla[0])
print(len(tupla))

tupla_string = tuple(lista_string)
print(type(tupla_string))