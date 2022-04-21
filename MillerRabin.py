import random
def miller_rabin(n,k):
    if n==2:
        return True
    if not n & 1:
        return  False

    def check(a,s,d,n):
        x=pow(a,d,n)
        print("%d----- %d" %(a,x))
        if x==1:
            return True
        for i in range(s-1):
            if x==n-1:
                return True
            x=pow(x,2,n)
            print("%d---- %d"%(a,x))
        return x==n-1

    s=0
    d=n-1
    while d%2==0:
        d>>1
        s+=1

    for i in range(k):
        a=random.randrange(2,n-1)
        if not check(a,s,d,n):
            return False
    return True


    
        
