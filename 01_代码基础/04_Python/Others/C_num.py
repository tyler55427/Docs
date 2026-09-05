import math

def c(n):
    l=[0]*(n+1)
    l[0]=l[n]=1
    for i in range(1,n//2+1):
        l[i]=l[n-i]=((l[i-1]*(n-i+1))//i)
    return l

def CCount(goal,toucishu,mode=6):
    count=0
    if goal<toucishu or goal>toucishu*mode:
        return 0
    elif goal==toucishu:
        return 1
    for i in range(0,goal-toucishu+1,mode):
        if (i//mode)%2==0:
            count+=math.comb(toucishu,i//mode)*math.comb(goal-i-1,toucishu-1)
        else:
            count-=math.comb(toucishu,i//mode)*math.comb(goal-i-1,toucishu-1)
    return count

def less_count(goal,toucishu):
    res=0
    for i in range(toucishu,goal+1):
        res+=CCount(i,toucishu)
    return res

def less_p(goal,toucishu,mode=6):
    return less_count(goal,toucishu)/(mode**toucishu)

print(less_p(350,105))
