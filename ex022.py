nome = input('Qual seu nome? ')
print('a) O nome com todas as letras maiusculas: ', format(nome.upper()))
print()
print('b) O nome com todas as letras minusculas: ', format(nome.lower()))
print()
print('c) Quantas letras ao todo sem espacos: ', len(nome.replace(' ', '')))
print()
print('d) Quantas letras tem no primeiro nome: ', len(nome.split()[0]))

