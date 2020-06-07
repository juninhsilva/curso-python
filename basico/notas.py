a = float(input('Primeiro BIM: '));
while (a > 10):
    a = float(input('\nNota errada.\nVale aeh 10;\nPrimeiro BIM: '));
b = float(input('Segundo BIM: '));
while (b > 10):
    b = float(input('\nNota errada.\nVale aeh 10;\Segundo BIM: '));
c = float(input('Terceiro BIM: '));
while (c > 10):
    c = float(input('\nNota errada.\nVale aeh 10;\Terceiro BIM: '));
d = float(input('Quarto BIM: '));
while (d > 10):
    d = float(input('\nNota errada.\nVale aeh 10;\Quarto BIM: '));
media = (a + b + c + d) / 4;
print('Mehdia: {}'.format(media));