n = raw_input().split(" ")
L = n[0]
N = n[1]
m = n[2]
c = n[3]
def fac(n):
    if (n == 1 or n == 0):
        return 1
    else:
        num = fac(n-1)*n
        return num
def exponent(x ,y):
    if (y == 0):
        return 1
    else:
        k = x*exponent(x,y-1)
        return k
def comb(n,r):
    k = fac(n)/(fac(n-r)*fac(r))
    return k
def f(L,N,m,c): 
    k = exponent(c,L)
    sum = 0
    for i in range(L-m):
        p = (comb(L,(m+i)))*(exponent((c-1),(L-(m+i))))
        sum = sum + p
    q = sum
    a = 0
    for i in range(L-N):
        r = (comb(L,(N+i)))*(exponent((c-1),(L-(N+i))))
        a = a+r
    s = a
    return k-(q+s)
for i in range(L):
    print (f((L-i),N,m,c))
    
        
