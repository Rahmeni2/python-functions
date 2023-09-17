def pgcd(a,b):
    while a%b!=0:
        if a>b:
            a=a-b
        elif a<b:
            b=b-a
    return b
#exemple 12 et 9
print(pgcd(12,9))