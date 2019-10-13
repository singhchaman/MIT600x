def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    i=1
    while(exp>0):
        i*=base
        exp-=1
    return i


def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp==0:
        return 1
    else:
        return base*recurPower(base,exp-1)


def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    if exp==0:
        return 1
    elif exp%2==0:
        return recurPowerNew(base*base,exp/2)
    else:
        return base*recurPowerNew(base,exp-1)


def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    gcd=min(a,b)
    while a%gcd!=0 or b%gcd!=0:
        gcd-=1
    return gcd


def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b==0:
        return a
    else:
        return gcdRecur(b,a%b)    


def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    c=0
    for i in aStr:
        c+=1
    return c        


def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    if aStr=='':
        return 0
    else:
        return 1+ lenRecur(aStr[1:])    


def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    mid=(len(aStr))/2
    if len(aStr)==0:
        return False
    elif aStr[mid]==char:
        return True
    elif aStr[mid]<char:
        return isIn(char,aStr[mid+1:])
    elif aStr[mid]>char:
        return isIn(char,aStr[:mid-1])
    else:
        return False        


def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    if len(str1)!=len(str2):
        return False
    else:
       if len(str1)==0 or len(str1)==1:
            return str1 == str2
       elif str1[0]==str2[-1]:
           return semordnilap(str1[1:],str2[:-1])
       else:
           return False