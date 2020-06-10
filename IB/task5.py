def change(name,ob,pr):
    i = subj.index(name)
    y = objs.index(ob)
    mat[i][y] = pr
    print('право изменено')

def rem(name,ob):
    i = subj.index(name)
    y = objs.index(ob)
    mat[i][y] = '-'
    print('право удалено')

def ad(name):
    subj.append(name)
    mat.append(['-','-','-','-'])
    print('Добавлен субъект %s под номером %d'%(name,subj.index(name)+1))

def delete(name):
    i = subj.index(name)
    mat.pop(i)
    subj.remove(name)
    print('Cубъект %s удален'%(name))

def percent():
    count = 0
    for i in range(len(subj)):
        for j in range(len(objs)):
            if mat[i][j] != '-':
                count+=1
    all=len(subj)*len(objs)
    print((count/all)*100,'%')

def acc(ob):
    lst = []
    j = objs.index(ob)
    for i in range(len(subj)):
        if mat[i][j] != '-':
            lst.append(subj[i])
    print(lst)

f = open('input.txt','r')
g = open('output.txt','w')

subj = f.readline().replace('\n','').split(' ')
objs = f.readline().replace('\n','').split(' ')
print(subj,objs)
mat=[]
for line in f:
    mas = line.replace('\n','').split(' ')
    mat.append(mas)
print(mat)
f.close()

com = str(input('Введите команду: '))
while com != 'quit':
    cmnd = com.split(' ')
    if cmnd[0] == 'change' and len(cmnd)==4: 
        change(cmnd[1],cmnd[2],cmnd[3])
    elif cmnd[0] == 'remove' and len(cmnd)==3:
        rem(cmnd[1],cmnd[2])
    elif cmnd[0] == 'add' and len(cmnd)==2:
        ad(cmnd[1])
    elif cmnd[0] == 'delete' and len(cmnd)==2:
        delete(cmnd[1])
    elif cmnd[0] == 'percent' and len(cmnd)==1: 
        percent()
    elif cmnd[0] == 'access' and len(cmnd)==2: 
        acc(cmnd[1])
    elif cmnd[0] == 'help' and len(cmnd)==1: 
        print('---change имя_субъекта имя_объекта право--- изменить право субъекта')
        print('---remove имя_субъекта имя_объекта--- удаление права субъекта')
        print('---add имя_субъекта--- добавление субъекта')
        print('---delete имя_субъекта--- удаление субъекта')
        print('---percent--- вычисление процента заполнености матрицы')
        print('---access имя_объекта--- список субъектов, имеющих доступ к этому объекту')
        print('---quit--- выход из программы')
    else:
        print('Команда введена неверно')  
    com = str(input('Введите команду: '))
for i in range(len(subj)): 
    g.write(subj[i]+' ')
g.write('\n')
for i in range(len(objs)): 
    g.write(objs[i]+' ')
g.write('\n')
for i in range(len(subj)):
    for j in range(len(objs)):
        g.write(mat[i][j]+' ')
    g.write('\n')
print('Программа завершила работу')
