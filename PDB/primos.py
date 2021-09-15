def es_primo(n):
    if n<1:
        return False
    elif n==2:
        return True
    else:
        for i in range(2,n):
            if n%i==0:
                return False
        return True

lista=[1,4,8,22,41,63,89]
primos=list(filter(es_primo,lista))

print(primos)