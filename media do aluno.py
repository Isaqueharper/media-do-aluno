cont = 0 
while cont < 10:
    nome = input('qual o nome do aluno? ')
    nota1 = float(input(f'qual a 1º nota do {nome}: '))
    nota2 = float(input(f'qual a 2º nota do {nome}: '))
    media = (nota1+nota2)/2
    print(f'a media do aluno {nome} e {media:.2f}')


    cont = cont + 1 
    