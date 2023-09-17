def premier(n):
     i=2
     while i<=(n//2) and n%i!=0:
         i=i+1
     return i>n//2
#exemple 11
print(premier(11))