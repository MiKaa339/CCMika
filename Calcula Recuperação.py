nome = input ('Olá, qual o seu nome?')
print ('Seja bem-vindo(a) {}, vamos calcular quantos pontos você precisa para não ficar de recuperação neste bimestre?'.format(nome))
n1 = float (input ('Primeiro, me diga sua nota na Prova Mensal:'))
n3 = float ( input ('Agora, digite sua nota de Atividade:'))
n2 = (30 - ((n1 * 2) + n3)) / 2
print ('Pronto, calculei aqui e você precisa tirar {} em sua Prova Bimestral para atingit 6.0 pontos e não ficar de recuperação'.format(n2))
print ('Agradeçemos o uso de nossa calculadora e te desejamos um bom estudo!')