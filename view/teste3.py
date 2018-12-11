n1 = float(input('Informe a nota 1:'))
n2 = float(input('Informe a nota 2: '))
n3 = float(input('Informe a nota 3: '))

media = (n1+n2+n3)/3

if media < 6:
    print('Média: ', media)
    print('Aluno reprovado.')
if media >= 7:
    print('Média:', media)
    print('Aluno aprovado.')