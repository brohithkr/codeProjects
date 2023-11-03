def numPossible(pos, low, high, k, n):
    if(k > high-pos and k>pos-low):
        return min(high-pos, pos-low) + 1
    if(k > high-pos):
        return high-pos+1
    if(k>pos-low):
        return pos-low+1
    else:
        return k

t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    arr = list(map(int, input().split()))   
    low, high = 0,n-1
    tot = 0
    i=0
    while i < (len(arr)):
        if(arr[i]%2==1):
            tot += numPossible(i,low, high, k, n)
            low = i+1
        i+=1
    print(tot)
