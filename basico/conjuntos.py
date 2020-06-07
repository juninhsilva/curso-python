conjunto_inteiros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
conjunto_reais = {1.0, 2, 3, 4}
print(type(conjunto_inteiros))
print(conjunto_inteiros)
conjunto_inteiros.add(0)
print(conjunto_inteiros)
conjunto_inteiros.discard(10)
print(conjunto_inteiros)
conjunto_inter = conjunto_inteiros.intersection(conjunto_reais)
print('Interseccao: {}'.format(conjunto_inter))
conjunto_difer = conjunto_inteiros.difference(conjunto_reais)
print('Diferenca: {}'.format(conjunto_difer))
conjunto_difer_sym = conjunto_inteiros.symmetric_difference(conjunto_reais)
print('Diferenca Simetrica: {}'.format(conjunto_difer_sym))
conjunto_union = conjunto_inteiros.union(conjunto_reais)
print('Uniao: {}'.format(conjunto_union))
conjunto_subset = conjunto_inteiros.issubset(conjunto_reais)
print('Subset: {}'.format(conjunto_subset))
conjunto_superset = conjunto_inteiros.issuperset(conjunto_reais)
print('Superset: {}'.format(conjunto_superset))
lista_string = ['cachorro', 'gato', 'elefante']
conjunto_string = set(lista_string)
print(conjunto_string)

conjunto_a = {1, 1, 3, 4, 5}
conjunto_b = {1, 3, 6}
conjunto_a.add(6)
conjunto_a.remove(1)
resultado = list(conjunto_a.intersection(conjunto_b))
print(resultado)