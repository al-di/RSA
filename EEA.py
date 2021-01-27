def eea(a, b, s, t):
    if(b==0):
        s=1
        t=0
    else:
        eea(b,a%b, s, t)
        hilf=s
        s=t
        t=hilf-int(a/b)*t
    return s, t;
