def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    res=a*x**2+b*x+c
    return res


def primesList(N):
    '''
    N: an integer
    '''
    res=[]
    for i in range(2,N+1):
        k=0
        for j in range(2,i):
            if i%j==0:
                k=1
                break
        if k==0:
            res.append(i)
    return res


res=[]
def count7(N):
    '''
    N: a non-negative integer
    '''
    if N/10 <1:
        if N%10==7:
            res.append(7)
    else:
        count7(N/10)
        count7(N%10)
    return res.count(7)


def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    k=aDict.keys()
    v=aDict.values()
    i=0
    while i<len(k):
        if v.count(aDict[k[i]])>1:
            k.remove(k[i])
            i-=1
        i+=1
    k.sort()
    return k


def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    for i in L:
        if not f(i):
            L.remove(i)
    return len(L)

run_satisfiesF(L, satisfiesF)