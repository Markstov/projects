from tkinter import *  
from tkinter import ttk
from tkinter import scrolledtext
import re

def clop():
    s =''
    for line in f:
        s+=line
    txt.insert(1.0,s) 

def trns():
    n = []
    txt1.delete(1.0,END)
    txt2.delete(1.0,END)
    txt3.delete(1.0,END)
    txc.delete(1.0,END)
    txn.delete(1.0,END)
    txin.delete(1.0,END)
    txw.delete(1.0,END)
    txr.delete(1.0,END)
    txo.delete(1.0,END)
    test = txt.get(1.0,END)
    res=''
    test = test.split('\n')
    for nm in range(len(test)):
        line = test[nm] + ' '
        if line[0]!='C':
            if line.find('"')>-1:
                result = re.search(r'".*"', line)
                if not (result.group(0) in c): c.append(result.group(0))
                line = re.sub(r'".*"','$c'+str(c.index(result.group(0))) ,line)
            mas = line.split(' ')
            for i in range(len(mas)):
                mas[i].lower()
                mas[i] = mas[i].rstrip()
                if (mas[i] in w or mas[i] in r or mas[i] in o or mas[i] in ind or mas[i] in n or mas[i] in c):
                    if (mas[i] in w):
                        res += ('w'+ str(w.index(mas[i]))+ ' ')
                    if (mas[i] in r):
                        res += ('r'+ str(r.index(mas[i]))+ ' ')
                    if (mas[i] in o):
                        res += ('o'+ str(o.index(mas[i]))+ ' ')
                    if (mas[i] in ind):
                        res += ('i'+ str(ind.index(mas[i]))+ ' ')
                    if (mas[i] in n):
                        res += ('n'+ str(n.index(mas[i]))+ ' ')
                    if (mas[i] in c):
                        res += ('c'+ str(c.index(mas[i]))+ ' ')
                elif ('$' in mas[i]):
                    res += mas[i][1:] + ' '
                elif (re.match(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', mas[i])):
                    n.append(mas[i])
                    res += ('n'+str (n.index(mas[i]))+ ' ')
                else:
                    if (re.match(r'\w+', mas[i])):
                        if (len(re.match(r'\w+', mas[i]).group(0))==len(mas[i])):
                            ind.append(mas[i])
                            res += ('i'+str (ind.index(mas[i]))+ ' ')
                        else:
                            news = re.match(r'\w+', mas[i]).group(0)
                            if (news in w):
                                res += ('w'+ str(w.index(news))+ ' ')
                            elif (news in ind):
                                res += ('i'+ str(ind.index(news))+ ' ')
                            else:
                                ind.append(news)
                                res += ('i'+str (ind.index(news))+ ' ')
                            ends = mas[i].replace(news,'')
                            for j in range(len(ends)):
                                if (ends[j] in r):
                                    res += ('r'+ str(r.index(ends[j]))+ ' ')
                                if (ends[j] in o):
                                    #op = re.match(r'[+]|-|[*]|/|=|[**]|::|.gt.|.lt.|.ge.|.le.|.ne.|.eq.', mas[i]).group(0)
                                    res += ('o'+ str(o.index(ends[j]))+ ' ')
        res+= '\n'

    txt1.insert(1.0,res) 
    
    so = ''
    for i in range(len(o)):
        so += 'o' + str(i) +' = ' + o[i] + '\n'
    txo.insert(1.0,so)

    sr = ''
    for i in range(len(r)):
        sr += 'r' + str(i) +' = ' + r[i] + '\n'
    txr.insert(1.0,sr)

    sw = ''
    for i in range(len(w)):
        sw += 'w' + str(i) +' = ' + w[i] + '\n'
    txw.insert(1.0,sw)

    sind = ''
    for i in range(len(ind)):
        sind += 'i' + str(i) +' = ' + ind[i] + '\n'
    txin.insert(1.0,sind)

    sn = ''
    for i in range(len(n)):
        sn += 'n' + str(i) +' = ' + n[i] + '\n'
    txn.insert(1.0,sn)

    sc = ''
    for i in range(len(c)):
        sc += 'c' + str(i) +' = ' + c[i] + '\n'
    txc.insert(1.0,sc)


    st = res.split("\n")    
    opz = ""
    num = 1
    up = 1
    stek = []    
    for i in st: 
        l = i.split(' ')
        t = 0
        k = 0
        for leks in l:
           # print(leks)
            if t == 0:
                if ('i' in leks or 'n' in leks or 'c' in leks):
                    opz += leks + ' '
                if leks == 'w4':
                    stek.insert(0,'НП')
                    stek.insert(0,num)
                    num+=1
                if leks == 'w15' or leks == 'w18':
                    stek.insert(0,leks)
                    t = 1
                if leks =='w0':
                    stek.insert(0,'DFL')
                    t = 1
                if leks =='w1':
                    stek.insert(0,'DFX')
                    t = 1
                if leks in StekPriority.keys():
                    if not (not stek):
                        if StekPriority.get(leks) > StekPriority.get(stek[0]):
                            stek.insert(0,leks)
                        else:
                            for j in range(len(stek)):
                                if 'o' in str(stek[j]):
                                    opz+= o[int(stek[j][1:])] + ' '
                                elif stek[j] == 'w12':
                                    opz+= ''
                                elif stek[j] == 'w13':
                                    opz+= 'M' + str(up) + 'УПЛ '
                                elif stek[j] == 'w14':
                                    opz+= 'M' + str(up) + 'БП '
                                    up +=1
                                else:
                                    opz+=str(stek[j]) + ' '
                            stek =[]
                            stek.insert(0,leks) 
                    else:
                        stek.insert(0,leks) 
            else:
                if ('i' in leks or 'n' in leks or 'c' in leks):
                    opz += leks + ' '
                    k+=1
        if t == 1:
            opz += str(k)+ ' '
        for j in range(len(stek)):
            if 'o' in str(stek[j]):
                opz+= o[int(stek[j][1:])] + ' '
            elif stek[j] == 'w12':
                opz+= ''
            elif stek[j] == 'w13':
                opz+= 'M' + str(up) + 'УПЛ '
            elif stek[j] == 'w14':
                opz+= 'M' + str(up) + 'БП '
                up +=1
            else:
                opz+=str(stek[j]) + ' '
        stek =[]
    opz = opz.replace('i0 2 НП ','КП')
    txt2.insert(1.0,opz)

    #########
    startSTR = opz.upper()
    stek =[]
    met2 = 1
    startSTR = startSTR.split(" ")
    mass_proc = []
    assembler_text = ""
    operation_check = False
    met_check = 0
    met_for1 = 0
    for i in startSTR:
    
      if i in massOP:
        if i == "НП":           
          for j in stek:
            if "I" in j:
              assembler_text+= "\n" + ind[int(j[1:])] + " " + "proc\n"  
              mass_proc = [ind[int(j[1:])]] + mass_proc
              stek = stek[1:]  
              assembler_text += ".data"        
              break
            stek = stek[1:]
        elif i == "<пц><пц>1+:=":
          assembler_text += "\n inc [i],1"
        elif i == "УПЛ<ц>":
          met_for1 +=1
          assembler_text += "\n cmp [i]," + n[int(stek[1][1:])]
          assembler_text += "\n je Met_FOR2" + str(met_for1)
          stek = stek[2:]
        elif i == "<пц>":
          met_for1+=1
          assembler_text += "\n Met_FOR1" + str(met_for1) + ": "
        elif i == "УПЛ":
        
          met_check+=1
          met1 = "Met_IF" + str(met_check)
        
          stek = stek[1:]
        
          if stek[0] == "O7":
          
            if operation_check:
              if "I" in stek[1]:
                assembler_text += "\n cmp ax, " + ind[int(stek[1][1:])]
                assembler_text += "\n jge " + met1
                stek = stek[2:]
              else:
                assembler_text += "\n cmp ax, " + n[int(stek[1][1:])]
                assembler_text += "\n jge " + met1
                stek = stek[2:]
            else:
              stek = stek[1:]
              if  "I" in stek[0] and "I" in stek[1]:              
                assembler_text += "\n mov " + "ax" + ", " + "[" + ind[int(stek[1][1:])] + "]"
                assembler_text += "\n cmp " + "ax" + ", " + "[" + ind[int(stek[0][1:])] + "]"
                assembler_text += "\n jge " + met1
                stek = stek[3:]
              elif "I" in stek[0] and "N" in stek[1]:              
                assembler_text += "\n mov " + "ax" + ", " + "[" + ind[int(stek[0][1:])] + "]"
                assembler_text += "\n cmp " + "ax" + ", " + n[int(stek[1][1:])] +"h"
                assembler_text += "\n jge " + met1
                stek = stek[3:]
              elif "I" in stek[1] and "N" in stek[0]:              
                assembler_text += "\n mov " + "ax" + ", " + "[" + ind[int(stek[1][1:])] + "]"
                assembler_text += "\n cmp " + "ax" + ", " + n[int(stek[0][1:])] +"h"
                assembler_text += "\n jge " + met1
                stek = stek[3:]
              elif "N" in stek[0] and "N" in stek[1]:              
                assembler_text += "\n mov " + "ax" + ", " + n[int(stek[0][1:])] +"h"
                assembler_text += "\n cmp " + "ax" + ", " + n[int(stek[1][1:])] +"h"
                assembler_text += "\n jge " + met1
                stek = stek[3:] 
          elif stek[0] == "O8":
            if operation_check:
              if "I" in stek[1]:
                assembler_text += "\n cmp ax, " + ind[int(stek[1][1:])]
                assembler_text += "\n jle " + met1
                stek = stek[2:]
              else:
                assembler_text += "\n cmp ax, " + n[int(stek[1][1:])]
                assembler_text += "\n jle " + met1
                stek = stek[2:]
            else:
              stek = stek[1:]
              if  "I" in stek[0] and "I" in stek[1]:              
                assembler_text += "\n mov " + "ax" + ", " + "[" + ind[int(stek[1][1:])] + "]"
                assembler_text += "\n cmp " + "ax" + ", " + "[" + ind[int(stek[0][1:])] + "]"
                assembler_text += "\n jle " + met1
                stek = stek[3:]
              elif "I" in stek[0] and "N" in stek[1]:              
                assembler_text += "\n mov " + "ax" + ", " + "[" + ind[int(stek[0][1:])] + "]"
                assembler_text += "\n cmp " + "ax" + ", " + n[int(stek[1][1:])] +"h"
                assembler_text += "\n jle " + met1
                stek = stek[3:]
              elif "I" in stek[1] and "N" in stek[0]:              
                assembler_text += "\n mov " + "ax" + ", " + "[" + ind[int(stek[1][1:])] + "]"
                assembler_text += "\n cmp " + "ax" + ", " + n[int(stek[0][1:])] +"h"
                assembler_text += "\n jle " + met1
                stek = stek[3:]
              elif "N" in stek[0] and "N" in stek[1]:              
                assembler_text += "\n mov " + "ax" + ", " + n[int(stek[0][1:])] +"h"
                assembler_text += "\n cmp " + "ax" + ", " + n[int(stek[1][1:])] +"h"
                assembler_text += "\n jle " + met1
                stek = stek[3:] 
          elif stek[0] == "O2":
            if operation_check:
              if "I" in stek[1]:
                assembler_text += "\n cmp ax, " + ind[int(stek[1][1:])]
                assembler_text += "\n jne " + met1
                stek = stek[2:]
              else:
                assembler_text += "\n cmp ax, " + n[int(stek[1][1:])]
                assembler_text += "\n jne " + met1
                stek = stek[2:]
            else:
              stek = stek[1:]
              if  "I" in stek[0] and "I" in stek[1]:              
                assembler_text += "\n mov " + "ax" + ", " + "[" + ind[int(stek[1][1:])] + "]"
                assembler_text += "\n cmp " + "ax" + ", " + "[" + ind[int(stek[0][1:])] + "]"
                assembler_text += "\n jne " + met1
                stek = stek[3:]
              elif "I" in stek[0] and "N" in stek[1]:              
                assembler_text += "\n mov " + "ax" + ", " + "[" + ind[int(stek[0][1:])] + "]"
                assembler_text += "\n cmp " + "ax" + ", " + n[int(stek[1][1:])] +"h"
                assembler_text += "\n jne " + met1
                stek = stek[3:]
              elif "I" in stek[1] and "N" in stek[0]:              
                assembler_text += "\n mov " + "ax" + ", " + "[" + ind[int(stek[1][1:])] + "]"
                assembler_text += "\n cmp " + "ax" + ", " + n[int(stek[0][1:])] +"h"
                assembler_text += "\n jne " + met1
                stek = stek[3:]
              elif "N" in stek[0] and "N" in stek[1]:              
                assembler_text += "\n mov " + "ax" + ", " + n[int(stek[0][1:])] +"h"
                assembler_text += "\n cmp " + "ax" + ", " + n[int(stek[1][1:])] +"h"
                assembler_text += "\n jne " + met1
                stek = stek[3:] 
          elif stek[0] == "O11":
            if operation_check:
              if "I" in stek[1]:
                assembler_text += "\n cmp ax, " + ind[int(stek[1][1:])]
                assembler_text += "\n je " + met1
                stek = stek[2:]
              else:
                assembler_text += "\n cmp ax, " + n[int(stek[1][1:])]
                assembler_text += "\n je " + met1
                stek = stek[2:]
            else:
              stek = stek[1:]
              if  "I" in stek[0] and "I" in stek[1]:              
                assembler_text += "\n mov " + "ax" + ", " + "[" + ind[int(stek[1][1:])] + "]"
                assembler_text += "\n cmp " + "ax" + ", " + "[" + ind[int(stek[0][1:])] + "]"
                assembler_text += "\n je " + met1
                stek = stek[3:]
              elif "I" in stek[0] and "N" in stek[1]:              
                assembler_text += "\n mov " + "ax" + ", " + "[" + ind[int(stek[0][1:])] + "]"
                assembler_text += "\n cmp " + "ax" + ", " + n[int(stek[1][1:])] +"h"
                assembler_text += "\n je " + met1
                stek = stek[3:]
              elif "I" in stek[1] and "N" in stek[0]:              
                assembler_text += "\n mov " + "ax" + ", " + "[" + ind[int(stek[1][1:])] + "]"
                assembler_text += "\n cmp " + "ax" + ", " + n[int(stek[0][1:])] +"h"
                assembler_text += "\n je " + met1
                stek = stek[3:]
              elif "N" in stek[0] and "N" in stek[1]:              
                assembler_text += "\n mov " + "ax" + ", " + n[int(stek[0][1:])] +"h"
                assembler_text += "\n cmp " + "ax" + ", " + n[int(stek[1][1:])] +"h"
                assembler_text += "\n je " + met1
                stek = stek[3:] 

        
        elif i == "M1:":
          assembler_text += "\n " + met1 + ":"
        elif i == "M2:":
          assembler_text += "\n Met_IF1" + str(met2) + ":"
        elif i == "БП":
          met2 += 1
          assembler_text+="\n jmp " + "Met_IF1" + str(met2)
        elif i == "M2<пц>:":
          assembler_text += "\n Met_FOR2" + str(met_for1) + ":"
        elif i == "БП<пц>":
          met2 += 1
          assembler_text+="\n jmp " + "Met_FOR1" + str(met_for1)
        elif i == "Ф":
          n = int(stek[0])
          stek=stek[1:]
          for i in range(n-1):
            if "I" in stek[i]:
              assembler_text+= "\npublic " +ind[int(stek[i][1:])]
            else:
              assembler_text+= "\npublic " +n[int(stek[i][1:])]
          stek = stek[n-1:]
          assembler_text+= "\njmp " + ind[int(stek[0][1:])]
          stek = stek[1:]
        elif i == "W0":
          nw9 = int(stek[0])
          stek = stek[1:]
          for j in stek:
            if nw9 == 0:
              break
            assembler_text += "\n" + "extern " + ind[int(j[1:])] + ":" + "DB"
            stek = stek[1:]
            nw9-=1
        elif i == "W1":
          nw9 = int(stek[0])
          stek = stek[1:]
          for j in stek:
            if nw9 == 0:
              break
            assembler_text += "\n" + "extern " + ind[int(j[1:])] + ":" + "DW"
            stek = stek[1:]
            nw9-=1
        elif i == "W2":
          nw9 = int(stek[0])
          stek = stek[1:]
          for j in stek:
            if nw9 == 0:
              break
            assembler_text += "\n" + "extern " + ind[int(j[1:])] + ":" + "DB"
            stek = stek[1:]
            nw9-=1
        elif i == "КО":
            assembler_text += "\n.code"
        elif i == "КП":
            assembler_text += "\n" + mass_proc[0] + " endp"
            mass_proc = mass_proc[1:]
        elif i == "O0":
          if operation_check == False and len(stek) > 1 and "I" in stek[0] and "I" in stek[1]:
            operation_check = True
            assembler_text += "\n mov " + "ax" + ", " + "[" + ind[int(stek[1][1:])] + "]"
            assembler_text += "\n add " + "ax" + ", " + "[" + ind[int(stek[0][1:])] + "]"
            stek = stek[2:]
          elif operation_check == False and len(stek) > 1 and "I" in stek[0] and "N" in stek[1]:
            operation_check = True
            assembler_text += "\n mov " + "ax" + ", " + "[" + ind[int(stek[0][1:])] + "]"
            assembler_text += "\n add " + "ax" + ", " + n[int(stek[1][1:])] +"h"
            stek = stek[2:]
          elif operation_check == False and len(stek) > 1 and "I" in stek[1] and "N" in stek[0]:
            operation_check = True
            assembler_text += "\n mov " + "ax" + ", " + "[" + ind[int(stek[1][1:])] + "]"
            assembler_text += "\n add " + "ax" + ", " + n[int(stek[0][1:])] +"h"
            stek = stek[2:]
          elif operation_check == False and len(stek) > 1 and "N" in stek[0] and "N" in stek[1]:
            operation_check = True
            assembler_text += "\n mov " + "ax" + ", " + n[int(stek[0][1:])] +"h"
            assembler_text += "\n add " + "ax" + ", " + n[int(stek[1][1:])] +"h"
            stek = stek[2:]
          else:
            if "I" in stek[0]:
              assembler_text += "\n add " + "ax" + ", " + "[" + ind[int(stek[0][1:])] + "]"
            elif "N" in stek[0]:
              assembler_text += "\n add " + "ax" + ", " + n[int(stek[0][1:])] +"h"
            stek = stek[1:]
        elif i == "O5":
          if operation_check == False and len(stek) > 1 and "I" in stek[0] and "I" in stek[1]:
            operation_check = True
            assembler_text += "\n mov " + "ax" + ", " + "[" + ind[int(stek[1][1:])] + "]"
            assembler_text += "\n mul " + "[" + ind[int(stek[0][1:])] + "]"
            stek = stek[2:]
          elif operation_check == False and len(stek) > 1 and "I" in stek[0] and "N" in stek[1]:
            operation_check = True
            assembler_text += "\n mov " + "ax" + ", " + "[" + ind[int(stek[0][1:])] + "]"
            assembler_text += "\n mul " +  n[int(stek[1][1:])] +"h"
            stek = stek[2:]
          elif operation_check == False and len(stek) > 1 and "I" in stek[1] and "N" in stek[0]:
            operation_check = True
            assembler_text += "\n mov " + "ax" + ", " + "[" + ind[int(stek[1][1:])] + "]"
            assembler_text += "\n mul " +  n[int(stek[0][1:])] +"h"
            stek = stek[2:]
          elif operation_check == False and len(stek) > 1 and "N" in stek[0] and "N" in stek[1]:
            operation_check = True
            assembler_text += "\n mov " + "ax" + ", " + n[int(stek[0][1:])] +"h"
            assembler_text += "\n mul " + n[int(stek[1][1:])] +"h"
            stek = stek[2:]
          else:
            if "I" in stek[0]:
              assembler_text += "\n mul " +  "[" + ind[int(stek[0][1:])] + "]"
            elif "N" in stek[0]:
              assembler_text += "\n mul " + n[int(stek[0][1:])] +"h"
            stek = stek[1:]
        elif i == "O1":
          if operation_check == False and len(stek) > 1 and "I" in stek[0] and "I" in stek[1]:
            operation_check = True
            assembler_text += "\n mov " + "ax" + ", " + "[" + ind[int(stek[1][1:])] + "]"
            assembler_text += "\n sub " + "ax" + ", " + "[" + ind[int(stek[0][1:])] + "]"
            stek = stek[2:]
          elif operation_check == False and len(stek) > 1 and "I" in stek[0] and "N" in stek[1]:
            operation_check = True
            assembler_text += "\n mov " + "ax" + ", " + n[int(stek[1][1:])] +"h"
            assembler_text += "\n sub " + "ax" + ", " + "[" + ind[int(stek[0][1:])] + "]"
            stek = stek[2:]
          elif operation_check == False and len(stek) > 1 and "I" in stek[1] and "N" in stek[0]:
            operation_check = True
            assembler_text += "\n mov " + "ax" + ", " + "[" + ind[int(stek[1][1:])] + "]"
            assembler_text += "\n sub " + "ax" + ", " + n[int(stek[0][1:])] +"h"
            stek = stek[2:]
          elif operation_check == False and len(stek) > 1 and "N" in stek[0] and "N" in stek[1]:
            operation_check = True
            assembler_text += "\n mov " + "ax" + ", " + n[int(stek[1][1:])] +"h"
            assembler_text += "\n sub " + "ax" + ", " + n[int(stek[0][1:])] +"h"
            stek = stek[2:]
          else:
            if "I" in stek[0]:
              assembler_text += "\n sub " + "ax" + ", " + "[" + ind[int(stek[0][1:])] + "]"
            elif "N" in stek[0]:
              assembler_text += "\n sub " + "ax" + ", " + n[int(stek[0][1:])] +"h"
            stek = stek[1:]
        elif i == "O3":
          if operation_check == False and len(stek) > 1 and "I" in stek[0] and "I" in stek[1]:
            operation_check = True
            assembler_text += "\n mov " + "ax" + ", " + "[" + ind[int(stek[1][1:])] + "]"
            assembler_text += "\n div "  + "[" + ind[int(stek[0][1:])] + "]"
            stek = stek[2:]
          elif operation_check == False and len(stek) > 1 and "I" in stek[0] and "N" in stek[1]:
            operation_check = True
            assembler_text += "\n mov " + "ax" + ", " + n[int(stek[1][1:])] +"h"
            assembler_text += "\n div " + "[" + ind[int(stek[0][1:])] + "]"
            stek = stek[2:]
          elif operation_check == False and len(stek) > 1 and "I" in stek[1] and "N" in stek[0]:
            operation_check = True
            assembler_text += "\n mov " + "ax" + ", " + "[" + ind[int(stek[1][1:])] + "]"
            assembler_text += "\n div " + n[int(stek[0][1:])] +"h"
            stek = stek[2:]
          elif operation_check == False and len(stek) > 1 and "N" in stek[0] and "N" in stek[1]:
            operation_check = True
            assembler_text += "\n mov " + "ax" + ", " + n[int(stek[1][1:])] +"h"
            assembler_text += "\n div " + n[int(stek[0][1:])] +"h"
            stek = stek[2:]
          else:
            if "I" in stek[0]:
              assembler_text += "\n div "  + "[" + ind[int(stek[0][1:])] + "]"
            elif "N" in stek[0]:
              assembler_text += "\n div "  + n[int(stek[0][1:])] +"h"
            stek = stek[1:]
        elif i == "O4":
          if len(stek) > 1 and "I" in stek[1] and "N" in stek[0]:
            assembler_text += "\n mov " + "[" + ind[int(stek[1][1:])] + "]" + ", " + n[int(stek[0][1:])] +"h"
            stek = stek[2:]
          elif len(stek) > 1 and "I" in stek[1] and "I" in stek[0]:
            assembler_text += "\n mov " + "[" + ind[int(stek[1][1:])] + "]" + ", " + "[" + ind[int(stek[0][1:])] + "]"
            stek = stek[2:]
          elif "I" in stek[0]:
            operation_check = False
            assembler_text += "\n mov " + "[" + ind[int(stek[0][1:])] + "]" + ", " + "ax" 
            stek = stek[1:]
      else:
        stek = [i] + stek
    txt3.insert(1.0,assembler_text)
    


            
             



o = ['+', '-', '**', '/', '=', '*', '::', '.gt.', '.lt.', '.ge.', '.le.', '.ne.', '.eq.']
r = [',','(',')',';','[',']']
w = ['integer', 'real', 'character', 'dimension', 'program', 'stop', 'end', 'function', 'parameter', 'return', 'subroutine', 'goto', 'if', 'then', 'else', 'read', 'while', 'do', 'print']
ind = []
c = []
massOP = ["НП","W0","W1","W2","КО","O4","O0","O1","O4","O5","O3","КП","Ф","M1:","УПЛ","БП","БП<пц>","M2:","M2<пц>:","УПЛ<ц>","<пц>","<пц><пц>1+:="]
StekPriority = {"r1":0,"АЭМ":0,"Ф":0,"w12":0,"r3":1,"r5":1,"w13":1,"w14":1,"o4":2,"w11":2,"or":3,"and":4,"not":5,"o7":6,"o8":6,"o9":6,"o10":6,"o11":6,"o12":6,"o0":7,"o1":7,"o3":8,"o5":8,"o2":9,"o6":10}
f = open('input.txt','r')
            


window = Tk()  
window.title("Транслятор")  
window.geometry('1600x800')  
tab_control = ttk.Notebook(window)  
tab1 = ttk.Frame(tab_control)  
tab2 = ttk.Frame(tab_control)  
tab_control.add(tab1, text='Транслятор')  
tab_control.add(tab2, text='Лексемы')  


lbl1 = Label(tab1, text='Исходный код')
lbl1.grid(column=0, row=0)
txt = scrolledtext.ScrolledText(tab1, width=45, height=40)  
txt.grid(column=0, row=1)

btn1 = Button(tab1, text="Открыть файл", command=clop)
btn1.grid(column=0, row=2)
 

lbl2 = Label(tab1, text='Результат')  
lbl2.grid(column=1, row=0)
txt1 = scrolledtext.ScrolledText(tab1, width=45, height=40)  
txt1.grid(column=1, row=1)

lbl3 = Label(tab1, text='ОПЗ')  
lbl3.grid(column=2, row=0)
txt2 = scrolledtext.ScrolledText(tab1, width=45, height=40)  
txt2.grid(column=2, row=1)

lbl4 = Label(tab1, text='Assembler')  
lbl4.grid(column=3, row=0)
txt3 = scrolledtext.ScrolledText(tab1, width=45, height=40)  
txt3.grid(column=3, row=1)

btn2 = Button(tab1, text="Старт", command=trns)
btn2.grid(column=1, row=2)


lbo = Label(tab2, text='Операции')  
lbo.grid(column=0, row=0)
txo = scrolledtext.ScrolledText(tab2, width=15, height=40)  
txo.grid(column=0, row=1)


lbr = Label(tab2, text='Разделители')  
lbr.grid(column=1, row=0)
txr = scrolledtext.ScrolledText(tab2, width=15, height=40)  
txr.grid(column=1, row=1)


lbw = Label(tab2, text='Команды')  
lbw.grid(column=2, row=0)
txw = scrolledtext.ScrolledText(tab2, width=20, height=40)  
txw.grid(column=2, row=1)


lbin = Label(tab2, text='Идентификаторы')  
lbin.grid(column=3, row=0)
txin = scrolledtext.ScrolledText(tab2, width=20, height=40)  
txin.grid(column=3, row=1)


lbn = Label(tab2, text='Числовые константы')  
lbn.grid(column=4, row=0)
txn = scrolledtext.ScrolledText(tab2, width=15, height=40)  
txn.grid(column=4, row=1)


lbc = Label(tab2, text='Числовые константы')  
lbc.grid(column=5, row=0)
txc = scrolledtext.ScrolledText(tab2, width=25, height=40)  
txc.grid(column=5, row=1)


tab_control.pack(expand=1, fill='both')  
window.mainloop()


                


