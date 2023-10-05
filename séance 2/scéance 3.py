#exo 1

n=100
L=[]
for i in range(n+1):
    if (i%3==0 or i%5==0) and i%15!=0:
        L.append(i)

#print(len(L))
#print(L)
#exo 2

def maximum(L):
    maxi=L[0]
    for x in L:
        if x>maxi:
            maxi=x
    return maxi
#print(maximum(L))
#print(max(L))
def minimum(L):
    mini=L[0]
    for x in L:
        if x<mini:
            mini=x
    return mini
#print(minimum(L))

#exo 3

def indice_max(L):
    n=len(L)
    indice=0
    for i in range(n):
        if L[i]>=L[indice] :
            indice=i
            
    return indice



L=[-3,-5,-2,-8,-1]
L=[-3,1,-5,1,-2,-8,-1]
print(indice_max(L))

#ex4
n=100
L=[i**2 for i in range(n+1)]
print(L)