from math import *
#for i in range(0,10,2):
 #   print(i)

#for i in range(1,10,2):
 #   print(i)

#for i in range(5,0,-1):
 #   print(i)

#for i in range(5,-1,-1):
 #   print(i)

#for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
 #   print(c)

U=1
#for n in range(10):
#    U=3*U+1
#print(U)


#ex4
n=0
Un=1
Unp1=exp(-Un)
while abs(Unp1-Un)>1e-6:
    Un=Unp1
    Unp1=exp(-Un)
    n=n+1
print(n)

#ex5

def methode_secante(f,U0,E):
    n=0
    h=1e-3
    Un=U0
    Unp1=Un-f(Un)/((f(Un+h)-f(Un))/h)
    while (abs(Unp1-Un)>E or abs(Unp1-Un)>E*Un)and n<50:
        Un=Unp1
        Unp1=Un-f(Un)/((f(Un+h)-f(Un))/h)
        n=n+1
    return Un
def f(t):
    return t**2-2
print(methode_secante(f,2,1e-7))
