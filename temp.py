import numpy as np

def factorial(N):
    if N==1:
        return N
    else:
        return N*factorial(N-1)

def sin(x,N):
    temp=0;
    for ii in range(0,N+1):
        temp=temp+(-1)**ii/factorial(2*ii+1)*x**(2*ii+1)
    return temp

def checkPalindrome(strin):##Do not try to assign the input str directly to old list and new list. The assignment 
     #of list in python just like pointer in C++, it assigns the memeory address  
    ls=list(strin);
    while (' ' in ls):
        ls.remove(' ')
        #ls.remove(',')
    ols=list(' '*len(ls));
    rls=list(' '*len(ls));
    for ii in range(0,len(ls)):
        ols[ii]=ls[ii];
    for ii in range(0,len(ls)):
        rls[ii]=ls[len(ls)-ii-1]
    print(rls)
    print(ols)
    return ols==rls

def checkPangram(strin):
    ls=list(set(strin));
    for  ii in ls:
        if (ord(ii) not in range(ord('a'),ord('z')+1)) and (ord(ii) not in range(ord('A'),ord('Z')+1)):
            ls.remove(ii)
    ls=list(set(str(ls).lower()));
    ls.remove("'")
    ls.remove(' ')
    ls.remove('[')
    ls.remove(']')
    ls.remove(',')
    print(sorted(ls))
    if len(ls)==26:
        return True
    else:
        return False
 def checkTemm(numin):
     return numin+1*24