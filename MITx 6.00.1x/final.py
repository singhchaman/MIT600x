def getSublists(L, n):
    res=[]
    for i in range(len(L)-n+1):
        res.append(L[i:i+n])
        i+=1
    return res


def longestRun(L):
    cnt=1
    max_cnt=0
    if len(L)==1:
        return 1
    else:
        for i in range(1,len(L)):
            if L[i]>=L[i-1]:
                cnt+=1
            else:
                cnt=1
            if cnt>max_cnt:
                max_cnt=cnt
    return max_cnt    


class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name    


def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    if atMe.myName() <= newFrob.myName():
        if atMe.getAfter() == None:
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
        elif atMe.getAfter().myName() >= newFrob.myName():
            newFrob.setBefore(atMe)
            newFrob.setAfter(atMe.getAfter())
            atMe.getAfter().setBefore(newFrob)
            atMe.setAfter(newFrob)
        else:
            insert(atMe.getAfter(), newFrob)
    else:
            if atMe.getBefore() == None:
                atMe.setBefore(newFrob)
                newFrob.setAfter(atMe)
            elif atMe.getBefore().myName() <= newFrob.myName():
                newFrob.setAfter(atMe)
                newFrob.setBefore(atMe.getBefore())
                atMe.getBefore().setAfter(newFrob)
                atMe.setBefore(newFrob) 
            else:
                insert(atMe.getBefore(), newFrob)        


def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list 
    """    
    if start.getBefore() == None:
        return start
    else:
        return findFront(start.getBefore())                