classes = {"служебные слова":"W","идентификаторы":"I","Операции":"O","Разделители":"R","Конастанты":"N","Конастанты1":"C"}
tableID = []
tableSLU = ["for", "to", "do", "while", "begin", "end", "var", "real", "string", "integer", "array", "of", "if", "then", "else","readln","writeln","read","goto","div","mod","program","downto"]
tableCONST = []
tableR = [";", ",", ":", "(", ")",".","[", "]"]
tableO = ["+", "-", "*", "/", "^", "<", ">", "=", "<>", "<=", ">=", ":="]
tableC = []




def FuncSem1(strID):
  global tableID
  if strID in tableID:
    return "I" + str(tableID.index(strID))
  else:
    tableID.append(strID)
    return "I" + str(tableID.index(strID))

def FuncSem2(strSL):
  global tableSLU
  if strSL in tableSLU:
    return "W" + str(tableSLU.index(strSL))
  else:
    return FuncSem1(strSL)


def FuncSem3(intCONST):
  global tableCONST
  if intCONST in tableCONST:
    return "N" + str(tableCONST.index(intCONST))
  else:
    tableCONST.append(intCONST)
    return "N" + str(tableCONST.index(intCONST))

def FuncSem4(strR):
  global tableR
  return "R" + str(tableR.index(strR))

def FuncSem5(strREM):

  return ""

def FuncSem6(strO):
  global tableO
  return "O" + str(tableO.index(strO))

def FuncSem7(strO):
  global tableO
  if strO in tableO:
    return "O" + str(tableO.index(strO))
  else:
    return "FAILED!"

def FuncSem8(strO):
  global tableO
  return "O" + str(tableO.index(strO))

def FuncSem9(strR):
  global tableR
  return "R" + str(tableR.index(strR))

def FuncSem10(strC):
  global tableC
  if strC in tableC:
    return "C" + str(tableC.index(strC))
  else:
    tableC.append(strC)
    return "C" + str(tableC.index(strC))

def FuncB(string, res_str):
  tx = string[0]
  check = True
  for i in string[1:]:
    
    if i <= "9" and i >= "0":
      check = False
      tx += i
    elif i >= 'a' and i <= 'z':
      tx += i
    elif i in tableO or i in tableR or i == " ":
      if check:            
        return func_main(string[string.index(i):],res_str+FuncSem2(tx))        
      else:    
        return func_main(string[string.index(i):],res_str+FuncSem1(tx))
    else:
      print("ОШИБКА!")
      

      return
  if check:        
        res_str += FuncSem2(tx)        
        return res_str        
  else:
        res_str += FuncSem1(tx)
        return res_str    


def FuncC(string,res_str, check):
  
  tx = string[0]
  
  for i in string[1:]:
    if i <= "9" and i >= "0" and check:
      tx+=i
    elif check and i == ".":
      tx+=i
      check = False
    elif i <= "9" and i >= "0":
      tx += i
    elif i in tableO or i in tableR or i == " ":
      return func_main(string[string.index(i):],res_str+FuncSem3(tx))
    else:
      print("ERROR!")
      return
  res_str += FuncSem3(tx)
  return res_str

def FuncDel(string,res_str):
  
  for i in string[1:]:
    
    if i == "}":
      return func_main(string[string.index(i)+1:],res_str)

def FuncOper(string, res_str):
  tx = string[0]
  for i in string[1:]:
    if i in tableO:
      tx+=i
    else:
      return func_main(string[string.index(i):], res_str + FuncSem7(tx))
def FuncStr(string,res_str):
  tx = "'"
  for i in string[1:]:
    
    
    if i == "'":
      tx+=i
      return func_main(string.replace(tx,""), res_str + FuncSem10(tx))
   
    tx+=i

text = "" #Prgm text

text1 = "'for i:= 1 to 100 do '"
def func_main(string,res_str):
  
  if len(string) != 0:
    if string[0] >= 'a' and string[0] <= 'z':
      
      res_str = FuncB(string, res_str) 
    elif string[0] == " ":
      
      res_str = func_main(string[1:], res_str)
    elif string[0] >= '0' and string[0] <= '9':
     
      res_str = FuncC(string, res_str,True)
    elif string[0] == "." and len(string) != 1:
      
      res_str = FuncC(string, res_str,False)
    elif string[0] == "{":
      
      res_str = FuncDel(string, res_str)
    elif string[0] in tableO or (string[0] == ":" and string[1] == "="):
      res_str =  FuncOper(string, res_str)
    elif string[0] in tableR:
      res_str = func_main(string[1:], res_str + FuncSem9(string[0]))
    elif string[0] == "'":
      res_str = FuncStr(string, res_str)
    else:
      print("ОШИБКА ВВОДА!")
      return
    
  else:
    return res_str
  print(tableCONST)
  return res_str

# print(func_main(text1, ""))
# print(tableID)
# final_text = ""

# for i in text.split('\n'):
#   res_str = ""
#   final_text += func_main(i,res_str)
#   final_text += "\n"

# print(final_text)
