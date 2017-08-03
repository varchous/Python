from math import *
def integral(n):
    a=1
    b=2
    x=a
    xn=(b-a)/n
    sum=0
    sumx=0
    xx=0
    j=10**-5 # эпсилон
    for i in range(n):
        #print(x,x+xn)
        sumx=((x+(x+xn))/2)
        y=cos(sumx) #функци
        sum=sum+y
        x=x+xn
    xx=xn*sum
    xx2=xx+1
    k=0
    flag=1
    while(flag==1):
        n=n*2
        sum=0
        sumx=0
        k=k+1
        x=a
        xn=(b-a)/n
        for i in range(n):
            sumx=((x+(x+xn))/2)
            y=cos(sumx) #функци
            sum=sum+y
            x=x+xn
        xx2=xn*sum
        if(j>xx2-xx):
            p1=xx2
            p2=k
            flag=0
            return p1,p2
        else:xx=xx2
print('Введите n')
n=int(input())
a1=integral(n)
print(a1)

