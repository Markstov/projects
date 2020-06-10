import translator as tr
stek = []
massOP = ["НП","W9","W7","W8","КО","O11","O0","O1","O11","O2","O3","КП","Ф","M1:","УПЛ","БП","БП<пц>","M2:","M2<пц>:","УПЛ<ц>","<пц>","<пц><пц>1+:="]

def assemb_tr(startSTR):
  met2 = 1
  startSTR = startSTR.split(" ")
  
  global stek
  global massOP
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
            assembler_text+= "\n" + tr.tableID[int(j[1:])] + " " + "proc\n"  
            mass_proc = [tr.tableID[int(j[1:])]] + mass_proc
            stek = stek[1:]  
            assembler_text += ".data"        
            break
          stek = stek[1:]
      elif i == "<пц><пц>1+:=":
        assembler_text += "\n inc [i],1"
      elif i == "УПЛ<ц>":
        met_for1 +=1
        assembler_text += "\n cmp [i]," + tr.tableCONST[int(stek[1][1:])]
        assembler_text += "\n je Met_FOR2" + str(met_for1)
        stek = stek[2:]
      elif i == "<пц>":
        met_for1+=1
        assembler_text += "\n Met_FOR1" + str(met_for1) + ": "
      elif i == "УПЛ":
        
        met_check+=1
        met1 = "Met_IF" + str(met_check)
        
        stek = stek[1:]
        
        if stek[0] == "O5":
          
          if operation_check:
            if "I" in stek[1]:
              assembler_text += "\n cmp ax, " + tr.tableID[int(stek[1][1:])]
              assembler_text += "\n jge " + met1
              stek = stek[2:]
            else:
              assembler_text += "\n cmp ax, " + tr.tableCONST[int(stek[1][1:])]
              assembler_text += "\n jge " + met1
              stek = stek[2:]
          else:
            stek = stek[1:]
            if  "I" in stek[0] and "I" in stek[1]:              
              assembler_text += "\n mov " + "ax" + ", " + "[" + tr.tableID[int(stek[1][1:])] + "]"
              assembler_text += "\n cmp " + "ax" + ", " + "[" + tr.tableID[int(stek[0][1:])] + "]"
              assembler_text += "\n jge " + met1
              stek = stek[3:]
            elif "I" in stek[0] and "N" in stek[1]:              
              assembler_text += "\n mov " + "ax" + ", " + "[" + tr.tableID[int(stek[0][1:])] + "]"
              assembler_text += "\n cmp " + "ax" + ", " + tr.tableCONST[int(stek[1][1:])] +"h"
              assembler_text += "\n jge " + met1
              stek = stek[3:]
            elif "I" in stek[1] and "N" in stek[0]:              
              assembler_text += "\n mov " + "ax" + ", " + "[" + tr.tableID[int(stek[1][1:])] + "]"
              assembler_text += "\n cmp " + "ax" + ", " + tr.tableCONST[int(stek[0][1:])] +"h"
              assembler_text += "\n jge " + met1
              stek = stek[3:]
            elif "N" in stek[0] and "N" in stek[1]:              
              assembler_text += "\n mov " + "ax" + ", " + tr.tableCONST[int(stek[0][1:])] +"h"
              assembler_text += "\n cmp " + "ax" + ", " + tr.tableCONST[int(stek[1][1:])] +"h"
              assembler_text += "\n jge " + met1
              stek = stek[3:] 
        elif stek[0] == "O6":
          if operation_check:
            if "I" in stek[1]:
              assembler_text += "\n cmp ax, " + tr.tableID[int(stek[1][1:])]
              assembler_text += "\n jle " + met1
              stek = stek[2:]
            else:
              assembler_text += "\n cmp ax, " + tr.tableCONST[int(stek[1][1:])]
              assembler_text += "\n jle " + met1
              stek = stek[2:]
          else:
            stek = stek[1:]
            if  "I" in stek[0] and "I" in stek[1]:              
              assembler_text += "\n mov " + "ax" + ", " + "[" + tr.tableID[int(stek[1][1:])] + "]"
              assembler_text += "\n cmp " + "ax" + ", " + "[" + tr.tableID[int(stek[0][1:])] + "]"
              assembler_text += "\n jle " + met1
              stek = stek[3:]
            elif "I" in stek[0] and "N" in stek[1]:              
              assembler_text += "\n mov " + "ax" + ", " + "[" + tr.tableID[int(stek[0][1:])] + "]"
              assembler_text += "\n cmp " + "ax" + ", " + tr.tableCONST[int(stek[1][1:])] +"h"
              assembler_text += "\n jle " + met1
              stek = stek[3:]
            elif "I" in stek[1] and "N" in stek[0]:              
              assembler_text += "\n mov " + "ax" + ", " + "[" + tr.tableID[int(stek[1][1:])] + "]"
              assembler_text += "\n cmp " + "ax" + ", " + tr.tableCONST[int(stek[0][1:])] +"h"
              assembler_text += "\n jle " + met1
              stek = stek[3:]
            elif "N" in stek[0] and "N" in stek[1]:              
              assembler_text += "\n mov " + "ax" + ", " + tr.tableCONST[int(stek[0][1:])] +"h"
              assembler_text += "\n cmp " + "ax" + ", " + tr.tableCONST[int(stek[1][1:])] +"h"
              assembler_text += "\n jle " + met1
              stek = stek[3:] 
        elif stek[0] == "O7":
          if operation_check:
            if "I" in stek[1]:
              assembler_text += "\n cmp ax, " + tr.tableID[int(stek[1][1:])]
              assembler_text += "\n jne " + met1
              stek = stek[2:]
            else:
              assembler_text += "\n cmp ax, " + tr.tableCONST[int(stek[1][1:])]
              assembler_text += "\n jne " + met1
              stek = stek[2:]
          else:
            stek = stek[1:]
            if  "I" in stek[0] and "I" in stek[1]:              
              assembler_text += "\n mov " + "ax" + ", " + "[" + tr.tableID[int(stek[1][1:])] + "]"
              assembler_text += "\n cmp " + "ax" + ", " + "[" + tr.tableID[int(stek[0][1:])] + "]"
              assembler_text += "\n jne " + met1
              stek = stek[3:]
            elif "I" in stek[0] and "N" in stek[1]:              
              assembler_text += "\n mov " + "ax" + ", " + "[" + tr.tableID[int(stek[0][1:])] + "]"
              assembler_text += "\n cmp " + "ax" + ", " + tr.tableCONST[int(stek[1][1:])] +"h"
              assembler_text += "\n jne " + met1
              stek = stek[3:]
            elif "I" in stek[1] and "N" in stek[0]:              
              assembler_text += "\n mov " + "ax" + ", " + "[" + tr.tableID[int(stek[1][1:])] + "]"
              assembler_text += "\n cmp " + "ax" + ", " + tr.tableCONST[int(stek[0][1:])] +"h"
              assembler_text += "\n jne " + met1
              stek = stek[3:]
            elif "N" in stek[0] and "N" in stek[1]:              
              assembler_text += "\n mov " + "ax" + ", " + tr.tableCONST[int(stek[0][1:])] +"h"
              assembler_text += "\n cmp " + "ax" + ", " + tr.tableCONST[int(stek[1][1:])] +"h"
              assembler_text += "\n jne " + met1
              stek = stek[3:] 
        elif stek[0] == "O8":
          if operation_check:
            if "I" in stek[1]:
              assembler_text += "\n cmp ax, " + tr.tableID[int(stek[1][1:])]
              assembler_text += "\n je " + met1
              stek = stek[2:]
            else:
              assembler_text += "\n cmp ax, " + tr.tableCONST[int(stek[1][1:])]
              assembler_text += "\n je " + met1
              stek = stek[2:]
          else:
            stek = stek[1:]
            if  "I" in stek[0] and "I" in stek[1]:              
              assembler_text += "\n mov " + "ax" + ", " + "[" + tr.tableID[int(stek[1][1:])] + "]"
              assembler_text += "\n cmp " + "ax" + ", " + "[" + tr.tableID[int(stek[0][1:])] + "]"
              assembler_text += "\n je " + met1
              stek = stek[3:]
            elif "I" in stek[0] and "N" in stek[1]:              
              assembler_text += "\n mov " + "ax" + ", " + "[" + tr.tableID[int(stek[0][1:])] + "]"
              assembler_text += "\n cmp " + "ax" + ", " + tr.tableCONST[int(stek[1][1:])] +"h"
              assembler_text += "\n je " + met1
              stek = stek[3:]
            elif "I" in stek[1] and "N" in stek[0]:              
              assembler_text += "\n mov " + "ax" + ", " + "[" + tr.tableID[int(stek[1][1:])] + "]"
              assembler_text += "\n cmp " + "ax" + ", " + tr.tableCONST[int(stek[0][1:])] +"h"
              assembler_text += "\n je " + met1
              stek = stek[3:]
            elif "N" in stek[0] and "N" in stek[1]:              
              assembler_text += "\n mov " + "ax" + ", " + tr.tableCONST[int(stek[0][1:])] +"h"
              assembler_text += "\n cmp " + "ax" + ", " + tr.tableCONST[int(stek[1][1:])] +"h"
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
            assembler_text+= "\npublic " +tr.tableID[int(stek[i][1:])]
          else:
            assembler_text+= "\npublic " +tr.tableCONST[int(stek[i][1:])]
        stek = stek[n-1:]
        assembler_text+= "\njmp " + tr.tableID[int(stek[0][1:])]
        stek = stek[1:]
      elif i == "W9":
        nw9 = int(stek[0])
        stek = stek[1:]
        for j in stek:
          if nw9 == 0:
            break
          assembler_text += "\n" + "extern " + tr.tableID[int(j[1:])] + ":" + "DB"
          stek = stek[1:]
          nw9-=1
      elif i == "W7":
        nw9 = int(stek[0])
        stek = stek[1:]
        for j in stek:
          if nw9 == 0:
            break
          assembler_text += "\n" + "extern " + tr.tableID[int(j[1:])] + ":" + "DW"
          stek = stek[1:]
          nw9-=1
      elif i == "W8":
        nw9 = int(stek[0])
        stek = stek[1:]
        for j in stek:
          if nw9 == 0:
            break
          assembler_text += "\n" + "extern " + tr.tableID[int(j[1:])] + ":" + "DB"
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
          assembler_text += "\n mov " + "ax" + ", " + "[" + tr.tableID[int(stek[1][1:])] + "]"
          assembler_text += "\n add " + "ax" + ", " + "[" + tr.tableID[int(stek[0][1:])] + "]"
          stek = stek[2:]
        elif operation_check == False and len(stek) > 1 and "I" in stek[0] and "N" in stek[1]:
          operation_check = True
          assembler_text += "\n mov " + "ax" + ", " + "[" + tr.tableID[int(stek[0][1:])] + "]"
          assembler_text += "\n add " + "ax" + ", " + tr.tableCONST[int(stek[1][1:])] +"h"
          stek = stek[2:]
        elif operation_check == False and len(stek) > 1 and "I" in stek[1] and "N" in stek[0]:
          operation_check = True
          assembler_text += "\n mov " + "ax" + ", " + "[" + tr.tableID[int(stek[1][1:])] + "]"
          assembler_text += "\n add " + "ax" + ", " + tr.tableCONST[int(stek[0][1:])] +"h"
          stek = stek[2:]
        elif operation_check == False and len(stek) > 1 and "N" in stek[0] and "N" in stek[1]:
          operation_check = True
          assembler_text += "\n mov " + "ax" + ", " + tr.tableCONST[int(stek[0][1:])] +"h"
          assembler_text += "\n add " + "ax" + ", " + tr.tableCONST[int(stek[1][1:])] +"h"
          stek = stek[2:]
        else:
          if "I" in stek[0]:
            assembler_text += "\n add " + "ax" + ", " + "[" + tr.tableID[int(stek[0][1:])] + "]"
          elif "N" in stek[0]:
            assembler_text += "\n add " + "ax" + ", " + tr.tableCONST[int(stek[0][1:])] +"h"
          stek = stek[1:]
      elif i == "O2":
        if operation_check == False and len(stek) > 1 and "I" in stek[0] and "I" in stek[1]:
          operation_check = True
          assembler_text += "\n mov " + "ax" + ", " + "[" + tr.tableID[int(stek[1][1:])] + "]"
          assembler_text += "\n mul " + "[" + tr.tableID[int(stek[0][1:])] + "]"
          stek = stek[2:]
        elif operation_check == False and len(stek) > 1 and "I" in stek[0] and "N" in stek[1]:
          operation_check = True
          assembler_text += "\n mov " + "ax" + ", " + "[" + tr.tableID[int(stek[0][1:])] + "]"
          assembler_text += "\n mul " +  tr.tableCONST[int(stek[1][1:])] +"h"
          stek = stek[2:]
        elif operation_check == False and len(stek) > 1 and "I" in stek[1] and "N" in stek[0]:
          operation_check = True
          assembler_text += "\n mov " + "ax" + ", " + "[" + tr.tableID[int(stek[1][1:])] + "]"
          assembler_text += "\n mul " +  tr.tableCONST[int(stek[0][1:])] +"h"
          stek = stek[2:]
        elif operation_check == False and len(stek) > 1 and "N" in stek[0] and "N" in stek[1]:
          operation_check = True
          assembler_text += "\n mov " + "ax" + ", " + tr.tableCONST[int(stek[0][1:])] +"h"
          assembler_text += "\n mul " + tr.tableCONST[int(stek[1][1:])] +"h"
          stek = stek[2:]
        else:
          if "I" in stek[0]:
            assembler_text += "\n mul " +  "[" + tr.tableID[int(stek[0][1:])] + "]"
          elif "N" in stek[0]:
            assembler_text += "\n mul " + tr.tableCONST[int(stek[0][1:])] +"h"
          stek = stek[1:]
      elif i == "O1":
        if operation_check == False and len(stek) > 1 and "I" in stek[0] and "I" in stek[1]:
          operation_check = True
          assembler_text += "\n mov " + "ax" + ", " + "[" + tr.tableID[int(stek[1][1:])] + "]"
          assembler_text += "\n sub " + "ax" + ", " + "[" + tr.tableID[int(stek[0][1:])] + "]"
          stek = stek[2:]
        elif operation_check == False and len(stek) > 1 and "I" in stek[0] and "N" in stek[1]:
          operation_check = True
          assembler_text += "\n mov " + "ax" + ", " + tr.tableCONST[int(stek[1][1:])] +"h"
          assembler_text += "\n sub " + "ax" + ", " + "[" + tr.tableID[int(stek[0][1:])] + "]"
          stek = stek[2:]
        elif operation_check == False and len(stek) > 1 and "I" in stek[1] and "N" in stek[0]:
          operation_check = True
          assembler_text += "\n mov " + "ax" + ", " + "[" + tr.tableID[int(stek[1][1:])] + "]"
          assembler_text += "\n sub " + "ax" + ", " + tr.tableCONST[int(stek[0][1:])] +"h"
          stek = stek[2:]
        elif operation_check == False and len(stek) > 1 and "N" in stek[0] and "N" in stek[1]:
          operation_check = True
          assembler_text += "\n mov " + "ax" + ", " + tr.tableCONST[int(stek[1][1:])] +"h"
          assembler_text += "\n sub " + "ax" + ", " + tr.tableCONST[int(stek[0][1:])] +"h"
          stek = stek[2:]
        else:
          if "I" in stek[0]:
            assembler_text += "\n sub " + "ax" + ", " + "[" + tr.tableID[int(stek[0][1:])] + "]"
          elif "N" in stek[0]:
            assembler_text += "\n sub " + "ax" + ", " + tr.tableCONST[int(stek[0][1:])] +"h"
          stek = stek[1:]
      elif i == "O3":
        if operation_check == False and len(stek) > 1 and "I" in stek[0] and "I" in stek[1]:
          operation_check = True
          assembler_text += "\n mov " + "ax" + ", " + "[" + tr.tableID[int(stek[1][1:])] + "]"
          assembler_text += "\n div "  + "[" + tr.tableID[int(stek[0][1:])] + "]"
          stek = stek[2:]
        elif operation_check == False and len(stek) > 1 and "I" in stek[0] and "N" in stek[1]:
          operation_check = True
          assembler_text += "\n mov " + "ax" + ", " + tr.tableCONST[int(stek[1][1:])] +"h"
          assembler_text += "\n div " + "[" + tr.tableID[int(stek[0][1:])] + "]"
          stek = stek[2:]
        elif operation_check == False and len(stek) > 1 and "I" in stek[1] and "N" in stek[0]:
          operation_check = True
          assembler_text += "\n mov " + "ax" + ", " + "[" + tr.tableID[int(stek[1][1:])] + "]"
          assembler_text += "\n div " + tr.tableCONST[int(stek[0][1:])] +"h"
          stek = stek[2:]
        elif operation_check == False and len(stek) > 1 and "N" in stek[0] and "N" in stek[1]:
          operation_check = True
          assembler_text += "\n mov " + "ax" + ", " + tr.tableCONST[int(stek[1][1:])] +"h"
          assembler_text += "\n div " + tr.tableCONST[int(stek[0][1:])] +"h"
          stek = stek[2:]
        else:
          if "I" in stek[0]:
            assembler_text += "\n div "  + "[" + tr.tableID[int(stek[0][1:])] + "]"
          elif "N" in stek[0]:
            assembler_text += "\n div "  + tr.tableCONST[int(stek[0][1:])] +"h"
          stek = stek[1:]
      elif i == "O11":
        if len(stek) > 1 and "I" in stek[1] and "N" in stek[0]:
          assembler_text += "\n mov " + "[" + tr.tableID[int(stek[1][1:])] + "]" + ", " + tr.tableCONST[int(stek[0][1:])] +"h"
          stek = stek[2:]
        elif len(stek) > 1 and "I" in stek[1] and "I" in stek[0]:
          assembler_text += "\n mov " + "[" + tr.tableID[int(stek[1][1:])] + "]" + ", " + "[" + tr.tableID[int(stek[0][1:])] + "]"
          stek = stek[2:]
        elif "I" in stek[0]:
          operation_check = False
          assembler_text += "\n mov " + "[" + tr.tableID[int(stek[0][1:])] + "]" + ", " + "ax" 
          stek = stek[1:]
    else:
      stek = [i] + stek
  return assembler_text