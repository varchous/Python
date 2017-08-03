f=open('10slov.txt', 'r')
s=f.read()
s=s.lower()
print(s)
f.close()
k=[".",",","(",")","!","?",":",";","'",'"',"1","2","3","4","5","6","7","8","9","0","-","+","=","*","/","%"]
for i in k:
    s=s.replace(i,'')
l=(s.split())  
L=set(l)
K=[]
for i in L:
    K.append((l.count(i),i))
K.sort(reverse=True)
for i in range (0,10):
    print (K[i][1],"-",K[i][0],"times")
    
