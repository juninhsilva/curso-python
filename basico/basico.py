a= float(input('Valor 1:: '));
b = float(input('Valor 2:: '));

soma = a + b;
subtracao = a - b;
multiplicacao = a * b;
divisao = a / b;
resto = a % b;

print('soma: '+ str(soma));
print('subtracao: '+ str(subtracao));
print('multiplicacao: ' + str(multiplicacao));
print('divisao: ' + str(divisao));
print('resto: ' + str(resto));

print('soma com format {}'.format(soma));
print('subtracao com format {}'.format(subtracao));
print('multiplicacao com format {}'.format(multiplicacao));
print('divisao com format {}'.format(divisao));
print('resto com format {}'.format(resto));