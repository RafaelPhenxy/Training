import random
import time
#challenges

Num = int(input('Tenta acertar o número que eu pensei 0-5: '))
Random = random.randint(0, 5)
print ('Pensando...')
time.sleep(2)
if Num == Random:
    print('Parabens! Você pensou no mesmo que eu!'.format(Random, Num))
else:
    print('AAA... Você errou, eu pensei em {} e você em {}'.format(Random, Num))
#
Kms = float(input('Você ta andando em que velocidade?: '))
if Kms <= 79:
    print('Você esta na velocidade certa!')
elif Kms == 80:
    print('Não passe dessa velocidade!')
else:
    print('Você passou do limite que era 80 Km')
    print('Você vai tomar uma multa de R${:.2f}'.format((Kms-80)*7))
#
nm = int(input('Escolhe um numero que eu falo se é impar ou par: '))
if nm % 2 == 0:
    print('PAR!')
else:
    print('IMPAR')
#
kms = float(input('Qual a distancia da viagem?(Km mais barato se passar de duzentos): '))
if kms <= 200:
    print('Sua tarifa vai ser R${:.2f}'.format(kms*0.5))
else:
    print ('Sua tarifa vai ser R${:.2f}'.format(kms*0.45))
#
import datetime
ano = int(input('Escolhe um ano pra saber se é bissexto(coloque 0 se quiser o ano atual): '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano bissexto({})'.format(ano))
else:
    print('Não é bissexto({})'.format(ano))
#
n1 = int(input('Coloca um numero: '))
n2 = int(input('Coloque outro: '))
n3 = int(input('Coloque outro: '))
Menor = n1
if n2<n1 and n2<n3:
    Menor = n2
if n3<n1 and n3<n2:
    Menor = n3
Maior = n1
if n2>n1 and n2>n3:
    Maior = n2
if n3>n1 and n3>n2:
    Maior = n3
print('Maior número digitado é: {}'.format(Maior))
print('Menor número digitado é: {}'.format(Menor))
#
sala = float(input('Digite o seu salário: '))
if sala <= 1250:
    print('Seu salário era de {:.2f} agora é {:.2f} com aumento de 15%'.format(sala, sala+((sala*15)/100)))
else:
    print('Seu salário era de {:.2f} agora é {:.2f} com aumento de 10%'.format(sala, sala+((sala*10)/100)))
#
r1 = int(input('Fale um lado de um triangulo: '))
r2 = int(input('Outro lado: '))
r3 = int(input('Fale o ultimo: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Juntando os segmentos forma um triangulo')
else:
    print('Não forma um triangulo')