import random
L=[]
n=0
print('Введите n(не меньше 15)')
while(n<15):
    n=int(input())
    if(n<15):print('ошибка','n < 15')
A=0
B=100
for i in range(n):
        x1=random.randint(A,B)
        L.append(x1)    
i=1
x=L[0] #значени последнего эл из упорядоченной последовательности
x1=1 #Кол-во элементов в упорядоченной последовательности 
y=0 #Номер эл  начала упорядоченной последовательности
y1=1 #Максимальное кол-во упорядоченных элементов
y2=0 #Первый эл самой длинной последовательности
print(L)
while(i<=(len(L))-1): #цикл для нахождения самой большой упорядоченной последовательности
    if(L[i]<x): #Если значени i-ого эл меньше значения последнего эл последовательности, то делаем его  началом последовательности(обнуляем значения старой) 
        x=L[i]
        x1=1
        y=i
    else: # Если он больше увеличиваем кол-во эл в последовательности и делаем его последним элементов
        x1=x1+1
        x=L[i]
    if(y1<x1): #Запоминаем самую длинную последовательность
        y1=x1
        y2=y
    i=i+1
L1=[] # Отсортированный спислк
for i in range(y2,y2+y1): # Вынимаем из списка элементы самой длинной последовательности и вставляем в отсортированный  список
    L1.append(L.pop(y2))
print(L1,L)
while(len(L)!=0): #Цикл для вставки остальных элементов в  отсортированный список 
    print(L[0],'->',L1)
    for i in range(len(L1)): # Цикл для поиска позиции куда надо вставить эл из спика
        flag=0 #Флаг необходимый, если вставляемый элемент больше всхе эл из отсортированного списка
        if(L[0]<=L1[i]): #Если эл списка меньше i-ого  эл отсортированного спика, то вставляем перед его перед i-им эл
            L1.insert(i,L.pop(0))
            flag=1
            break
    if(flag==0):L1.append(L.pop(0)) #Если  не найденно меньшего эл, то вставляем в конец отсортированного списка
print(L1)    


