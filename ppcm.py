def ppcm(a,b):
    m=a
    while m%b!=0:
        m=m+a
    return m
#exemple 2 et 4
print(ppcm(2,4))