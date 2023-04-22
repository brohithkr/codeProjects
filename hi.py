
def subsequences(s,res):
    if len(s) == 0:
        return res
    charf = s[0]
    print(charf,s[1:])
    res2 = subsequences(s[1:], res)
    # res2arr = res2.split(",")
    print(res2)
    for i in res2:
        res+=[i]
        # res+=","
        res+= [charf + i]
        # res+=","
    return res
    
if __name__ == "__main__":
    s = "hello"

    res = []

    res2 = subsequences(s, res)
    # print(res2)