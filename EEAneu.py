def eea(a, b):
    if(b==0):
        return (a, 1, 0)
    
    (d, sSt, tSt)=eea(b, a%b)

    s = tSt
    t = sSt-(int(a/b))*tSt

    return (d, s, t)


print(eea(13,60))
print(eea(41,192))

