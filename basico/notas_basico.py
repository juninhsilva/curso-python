a = float(input('Primeiro BIM: '));
if (a > 10):
    a = float(input('\nNota errada.\nVale aeh 10;\nPrimeiro BIM: '));
b = float(input('Segundo BIM: '));
if (b > 10):
    b = float(input('\nNota errada.\nVale aeh 10;\Segundo BIM: '));
c = float(input('Terceiro BIM: '));
if (c > 10):
    c = float(input('\nNota errada.\nVale aeh 10;\Terceiro BIM: '));
d = float(input('Quarto BIM: '));
if (d > 10):
    d = float(input('\nNota errada.\nVale aeh 10;\Quarto BIM: '));
if(a <= 10 and b <= 10 and c <= 10 and d <= 10):
    media = (a + b + c + d) / 4;
    print('Mehdia: {}'.format(media));