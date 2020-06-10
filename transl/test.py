#import re
#o = ['+', '-', '**', '/', '=', '*', '::', '.gt.', '.lt.', '.ge.', '.le.', '.ne.', '.eq.']
#x = 'szera_213'
#result = re.match(r'\w+', x).group(0)
#print(result)
#if (len(re.match(r'\w+', x).group(0))==len(x)):
#    print('yes')
#c='.'
#if (c in o):
#    print('!!!!!')
#z = '**dad'
#op = re.match(r'[+]|-|[*]{1,2}|/|=||::|.gt.|.lt.|.ge.|.le.|.ne.|.eq.', z).group(0)
#print(op)
 
#ns = ''
#for i in range(len(o)):
#    ns += 'o' + str(i) +' = ' + o[i] + '\n'
#print(ns)
#\w+
#[a-z]+[_]+[0-9]+|[a-z]+[0-9]+|[a-z]+
#a-z*\d+|_+|a-z+
# mas=[1,2,3]
# for i in range(len(mas)):
#     print(mas[i])

# line='fr "ad a" dfd asx dsa'
# c =['"ad a"','"fdfdf"']
# if line.find('"')>-1:
#     result = re.search(r'".*"', line)
#     if not (result.group(0) in c): c.append(result.group(0))
#     line = re.sub(r'".*"','$c'+str(c.index(result.group(0))) ,line)
# print(line.upper()[1:])
# print(c)
# w = ['+','-','*','/','=','**','.GT.','.LT.','.GE.','.LE.','.NE.','.EQ.']
# new_li = [x.lower() for x in w]
# print(new_li)

# i=1
# s='rfrf'
# s+=('w'+str(i)+' ')
# print(s)

# StekPriority = {"r1":0,"АЭМ":0,"Ф":0,"w12":0,"r3":1,"r5":1,"w13":1,"w14":1,"o4":2,"w11":2,"or":3,"and":4,"not":5,"o7":6,"o8":6,"o9":6,"o10":6,"o11":6,"o12":6,"o0":7,"o1":7,"o3":8,"o5":8,"o2":9,"o6":10}
# stek = ['']
# if StekPriority.get(leks) > StekPriority.get(stek[0]):
#      stek.insert(0,leks)

o = ['+', '-', '**', '/', '=', '*', '::', '.gt.', '.lt.', '.ge.', '.le.', '.ne.', '.eq.']
r = [',','(',')',';','[',']']
w = ['integer', 'real', 'character', 'dimension', 'program', 'stop', 'end', 'function', 'parameter', 'return', 'subroutine', 'goto', 'if', 'then', 'else', 'read', 'while', 'do', 'print']
ind = []
n = []
c = []
massOP1 = ["НП","W9","W7","W8","КО","O11","O0","O1","O11","O2","O3","КП","Ф","M1:","УПЛ","БП","БП<пц>","M2:","M2<пц>:","УПЛ<ц>","<пц>","<пц><пц>1+:="]
massOP = ["НП","W0","W1","W2","КО","O4","O0","O1","O4","O5","O3","КП","Ф","M1:","УПЛ","БП","БП<пц>","M2:","M2<пц>:","УПЛ<ц>","<пц>","<пц><пц>1+:="]
print(massOP1)
print(massOP)