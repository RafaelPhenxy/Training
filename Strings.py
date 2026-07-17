Name = "Rafael De Souza Carlos"
print(Name[:6:2])
print(Name[6::3])
print(Name[7:])
print(Name[:6])

print ("""More than just technical knowledge, I bring a problem-solving mindset and a commitment to continuous learning to the team. I am currently in a phase of intensive growth, where my dedication, discipline, and drive to deliver high-quality results are my greatest assets.

I am someone who seeks to understand the 'why' behind every line of code, which allows me to not only execute tasks but also propose improvements. I adapt easily to new tools and am fully committed to growing with the company, contributing from day one with energy, focus, and a willingness to learn from daily challenges.""")


print (Name.count("a"))
print (len(Name))
print (Name.replace("Carlos", "Coder"))
print ("Rafael" in Name)
print (Name.lower().find("de"))
print (Name.split())
Na = Name.split()
print (Na[0]+Na[1]+Na[2]+Na[3])
#challenges
na = str(input('Enter your name: ')).strip()
print ('Your name in capital letters: {}'.format(na.upper()))
print ('Your name in lowercase letters: {}'.format(na.lower()))
ns = na.split()
allnumb = ''.join(ns)
print ('Adding all letters you have: {} letters.'.format(len(allnumb)))
print ('Your first name is: {} and have: {} letters.'.format(ns[0], len(ns[0])))
#
num = int(input('Enter a number on 0-9999: '))
U = num // 1 % 10
D = num // 10 % 10
C = num // 100 % 10
M = num // 1000 % 10
print ('Units is: {}'.format(U))
print ('Tens is: {}'.format(D))
print ('Hundreds is: {}'.format(C))
print ('thousand is: {}'.format(M))
#
nm = str(input('Qual cidade que você nasceu? ')).strip()
print (nm[:5].lower() == 'santo')
#
no = str(input('Qual seu nome? '))
print ('Tem Silva no nome? {}'.format('silva' in no.lower()))
#
wr = str(input('enter anything word: ')).lower().strip()
print ('First A in {}'.format(wr.find('a')+1))
print ('Last A in {}'.format(wr.rfind('a')+1))
print ('Total A is: {}'.format(wr.count('a')))
#
nm2 = str(input('Name: ')).strip()
nms = nm2.split()
print('Your first name is: {}'.format(nms[0]))
print ('and your last name is: {}'.format(nms[len(nms)-1]))

