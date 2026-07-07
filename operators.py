#order of operators
print (((2+(3*2+6**5))-4))
#square root
print (81**(1/2))
#cube root
print (8**(1/3))
#With str
print ("Rafael "*5)
#Challenge
Nm = float(input('Enter a number: '))
print (Nm+1)
print (Nm)
print (Nm-1)
print ("Nm: {}, NmA: {}, NmS: {}".format(Nm, Nm-1, Nm+1))
print (Nm*2)
print (Nm*3)
print (Nm**(1/2))
#Mean
Nm2 = float(input('Enter another number: '))
print ("Sua média é {}".format((Nm+Nm2)/2))
#Meters in Cm and in Mm
Met = float(input('Enter a number in meters: '))
Cm = Met*100
Mm = Met*1000
print ('In meters is {}'.format(Met))
print ("In Cm's is {}".format(Cm))
print ("In Mm's is {}".format(Mm))
#Multiplication table
numb = int(input('Enter a number for make a multiplication table 1-10: '))
print ('{}x1 is {}'.format(numb, numb*1))
print ('{}x2 is {}'.format(numb, numb*2))
print ("{}x3 is {}".format(numb, numb*3))
print ("{}x4 is {}".format(numb, numb*4))
print ("{}x5 is {}".format(numb, numb*5))
print ("{}x6 is {}".format(numb, numb*6))
print ("{}x7 is {}".format(numb, numb*7))
print ("{}x8 is {}".format(numb, numb*8))
print ("{}x9 is {}".format(numb, numb*9))
print ("{}x10 is {}".format(numb, numb*10))
#Real for dolar
Real = float(input('Your balance is reals: '))
print ("{:.3f} dolars".format(Real/5.14))
#
Al = float(input('Altura: '))
La = float(input('Largura: '))
ArQ = Al*La
print ("A area da parede é {} e vai precisar de {} litros".format(ArQ, ArQ/2))
#preço
Preço = float(input('Valor: '))
desconto = (Preço*5)/100
print ('Seu desconto é {} e o valor com desconto é {}'.format(desconto, Preço-desconto))
#salario
sala = float(input('Salario: '))
aumento = (sala*15)/100
print ("Seu salario era de {} mas você teve um aumento de 15%({}), agora seu salario é {}".format(sala, aumento, sala+aumento))
