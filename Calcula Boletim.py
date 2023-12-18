nome = input ('Olá, qual o seu nome?')
print ('Seja bem-vindo (a) {}, vamos calcular sua média bimestral do boletim?'.format(nome))
n1 = float ( input ( 'Primeiro, me diga sua nota da prova mensal:'))
n2 = float ( input ( 'Agora, me diga sua nota da prova bimestral:'))
n3 = float ( input ( 'Por fim, digite sua nota de atividade do bimestre:'))
média = (((n1 * 2) + (n2 * 2)) + n3) / 5
print ('Calculei aqui, e sua nota bimestral será de: {}'.format(média))