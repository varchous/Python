r=[0,0,['а','б','в','г'],['д','е','з','ж'],['и','й','к','л'],['м','н','о','п'],['р','с','т','у'],['ф','х','ц','ч'],['ш','щ','ъ','ы'],['ь','э','ю','я']]
rr=['а','б','в','г','д','е','з','ж','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
f=open('1.txt', 'r') 
s1=f.read()
l=(s1.split('\n')) #разбиваем словарь на слова.
for i in range (len(l)):
    l[i]=l[i].split(' ') #разбиваем каждое слово на слово и вероятность встречи слова.
    for j  in range(len(l[i][0])):
        #print(l[i][0][j])
        for z in range(len(rr)):
            if (rr[z]==l[i][0][j]): #Находим какой цифре соответсвует каждая буква слова(Ищем совпадение в списке rr и добавляем в список цифру, которой соответствует эта буква).
               # print(rr[z])
                l[i].append(str((z//4)+2))
print(l)
s=str(input())
#print(s)
l2=[]
for i in s: #Вносим введенную строку в список посимвольно.
    if(i=='1'):break 
    l2.append(str(i))
s2=''
y=''#Переменная для запоминания слова из словаря.
#print(len(l))
i=0
l3=[] #Список для наиболее вероятной последовательность символов.
while(i<len(l2)): #Проверяем посимвольно каждый символ введенного слова с соответствующими ему символами в каждой строке.
    #print('i=',i)
    j=0
    y2='0' #Переменная для проверки приоритета.
    while(j<len(l)):
        #print('i=',i,'len[j]-2=',int(len(l[j]))-2)
        if(i+1>int(len(l[j]))-2):#Если слово из словаря меньше введенного слова, то мы удаляем его из списка.
            l.pop(j)
            j=j+1
            continue
        #print('l[j][i+2]=',l[j][i+2],l[j][0])
        if(l2[i]==l[j][i+2])and(y2=='0'):#Если символ введенного слова совпадает с символом из словаря, то мы запоминаем слово и присваиваем его приоритет вероятности.
            y=l[j][0]
            y2=int(l[j][1])
        elif(l2[i]==l[j][i+2])and(y2<int(l[j][1])): #Если символ введенного слова совпадает с символом из словаря и приоритет у этого слова выше, то мы запоминаем слово и присваиваем его приоритет вероятности.
            y=l[j][0]
            y2=int(l[j][1])
        elif(l2[i]!=l[j][i+2]):#Если символ введенного слова не совпадает с символом из словаря, то мы удаляем его из списка.
            l.pop(j)
            continue
        j=j+1
    #print(i)
    if(len(l)!=0):#Если список вероятностей не пустой, то запоминаем определенное кол-во символом из переменной y.
        #print(y[:i+1],':',y)
        l3.append(y[:i+1])
    i=i+1
if(len(l)==0):#Если список не пуст, то выводим список с наиболее вероятной последовательность символов.
    print('MANUALLY')
else:
    for i in l3:
        print(i)



