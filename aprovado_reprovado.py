# Desenvolva um programa que armazene quatro notas em uma lista e que apresente a média final. Caso a média seja igual ou superior a 7, apresentar a mensagem "APROVADO", caso contrário, armazenar a nota da prova final e recalcular a média. Caso a nova média seja igual superior a 5, apresentar a mensagem "APROVADO", caso contrário, apresentar a mensagem "REPROVADO"

notas = []
contador = 1

while contador < 5:
    notas.append(float(input(f'Informe a {contador}ª nota: ')))
    contador += 1

media = sum(notas) / len(notas)

if media < 7:
    notas.append(float(input('Informe a nota da prova final: ')))
    media = sum(notas) / len(notas)
    if media > 5:
        print(f'Notas Final: {media:.1f}. Aluno Aprovado.')
    else:
        print(f'Notas Final: {media:.1f}. Aluno Reprovado.')
else:
    print(f'Notas Final: {media:.1f}. Aluno Aprovado.')