N1 = int(input("Enter a number: "))
N2 = int(input("Enter a another number: "))
Result = N1 + N2
M = N1 * N2
D = N1 / N2
DW = N1 // N2
P = N1 ** N2
print ("The addition of {:=>10} and {:=<10} is {:=^10}".format(N1, N2 ,Result))
print ("The addition is {}".format(N1+N2))
print ("Multiplication is {}\n and division is {:.3f}".format(M, D), end= ', ')
print ("division Whole is {} and potentiation is {}".format(DW, P))