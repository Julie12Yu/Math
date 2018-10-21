a = input("What is the 'a' of your equation?")
b1 = input("What is the 'b' of your equation?")
c = input("What is the 'c' of your equation?")

b3 = float(b1)**2
b2 = -float(b1)

a = float(a)
c = float(c)
situation1 = (b2+(b3-4*a*c)**(.5))/(2*a)
situation2 = (b2-(b3-4*a*c)**(.5))/(2*a)
print(str(situation1)+" is the first solution.")
print(str(situation2)+" is the second solution.")
