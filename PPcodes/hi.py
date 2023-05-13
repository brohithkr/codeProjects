def isprime(n):
    isprime = True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            isprime = False
            break
    return isprime

def primeFactor(n):
    lst = []
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            if isprime(i):
                lst.append(i)
                if isprime(n/i):
                    lst.append(int(n/i))
    return lst

# n = int(input())
print(primeFactor(315))
