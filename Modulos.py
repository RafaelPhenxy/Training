import math
import random
nm = int(input('Enter a number: '))
RSq: float = math.sqrt(nm)
print("Your number is: {} and your square root is: {:.2f}".format(nm, RSq))
NRd: int = random.randint(1, 1000)
print(NRd)
#Challenges
Num1 = float(input("Enter a number: "))
Int: int = math.trunc(Num1)
print ("Your number is:{}, and your int is:{}".format(Num1,Int))
#
nm1 = float(input("Cateto 1: "))
nm2 = float(input("Cateto 2: "))
Ct: float = math.hypot(nm1,nm2)
print (Ct)
#
n1 = str(input("Name 1: "))
n2 = str(input("Name 2: "))
n3 = str(input("Name 3: "))
n4 = str(input("Name 4: "))

list[str] = [n1, n2, n3, n4]
Choice: str = random.choice(list)
print (Choice)
#
na1 = str(input("Name 1: "))
na2 = str(input("Name 2: "))
na3 = str(input("Name 3: "))

list[str] = [na1, na2, na3]
RandomOrder: None = random.shuffle(list)
print (list)