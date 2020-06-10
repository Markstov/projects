stek = []
StekPriority = {"R3":0,"АЭМ":0,"Ф":0,"W12":0,"W4":0,"W12 M1":0,"W12 M2":0,"W0":0,"W0 <пц>M1M2":0,"W0 <пц>":0,"W1":1,"W2":1,"W5":1,"R4":1,"W13":1,"W14":1,"O11":2,"W18":2,"W24":3,"W23":4,"W25":5,"O9":6,"O10":6,"O5":6,"O6":6,"O7":6,"O8":6,"O0":7,"O1":7,"O2":8,"O3":8,"O4":9,"W27":11,"R2":11}
strok = "a+b<-5 and 2-c=1+q"


def opz(string):
    peremenay = 0
    global stek
    global StekPriority
    checkVAR1 = False
    checkIF = False
    checkIF1 = False
    checkIF11 = False
    checkIF12 = False
    checkFOR = False
    checkFOR1 = False
    checkPROC = False
    checkMainVar = False
    checkMainVar1 = 0
    checkPROC1 = 0
    checkPROC2 = 0
    checkFunc = 0
    checkMass = 0
    checkVAR = 0
    finishSTR = ""
    string = string.split("\n")
    
    checkSTR = ""
    for i in string:
      checkSTR += i + " "
    
    checkSTR = checkSTR.split(" ") 
    
    
    CDP = [value for value in checkSTR if value]
    
    checkSTR = CDP
    print(checkSTR)
    for i in checkSTR:
      peremenay+=1
      
      if i in StekPriority:
        if i == "R3" and "I" in checkSTR[checkSTR.index(i)-1] and not(checkPROC):
          checkFunc = 1
          stek = ["Ф"] + stek
        elif i == "W27":
          stek = [i] + stek
          checkPROC = True
          checkPROC1 += 1
          checkPROC2 += 1
        
        elif i == "W0":
          stek = ["W0 <пц>"] + stek
        elif i == "W1":
          for j in stek:
            if not("W0" in j): 
              finishSTR += j + " "
              stek = stek[1:]
            else:
              stek[0] += "M1"
              finishSTR += "M1 <пц> "
              break
        elif i == "W2":
          if "W4" == checkSTR[peremenay]:
            checkFOR = True
          else:
            checkFOR1 = True
          for j in stek:
            if not("W0" in j): 
              finishSTR += j + " "
              stek = stek[1:]
            else:
              stek[0] += "M2"
              finishSTR += "M2 УПЛ<ц> "
              break
        elif i == "W12":
          stek = [i] + stek  
        elif i == "W14":
          checkIF11 = False
          checkIF12 = False
          if "W4" == checkSTR[peremenay]:
            checkIF = True
          else:
            checkIF1 = True
          for j in stek:
            if j != "W12 M1":
              finishSTR += j + " "
              stek = stek[1:]
            else:
              finishSTR += "M2 БП M1: "
              stek[0] = stek[0].replace("M1","M2")
              break
        
        elif i == "W5" and checkIF11 and checkSTR[peremenay] != "W14":
          
          for j in stek:              
            if not("W12" in j):
              if j == "W4":
                stek = stek[1:]
              else:
                finishSTR += j + " "
                stek = stek[1:]
            else:
              finishSTR += "M1: "
              stek = stek[1:]
              checkIF11 = False
              break
        elif i == "W4" and checkMainVar:
          checkMainVar = False
          checkMainVar1 = 0
          finishSTR += "КО" + " "

        elif i == "W5" and checkIF:
          
          for j in stek:
            
            if not("W12" in j):
              if j == "W4":
                stek = stek[1:]
              else:
                finishSTR += j + " "
                stek = stek[1:]
            else:
              finishSTR += "M2: "
              stek = stek[1:]
              checkIF = False
              break

        elif i == "W5" and checkFOR:
          
          for j in stek:
            
            if not("W0" in j):
              if j == "W4":
                stek = stek[1:]
              else:
                finishSTR += j + " "
                stek = stek[1:]
            else:
              finishSTR+="<пц><пц>1+:= M1 БП<пц> M2<пц>: "
              stek = stek[1:]
              checkFOR = False
              break
        elif i == "W5" and "R5" == checkSTR[peremenay]:
          
          for j in stek:
            if j != "W27":
              if j != "W4":
                finishSTR += j + " "
                stek = stek[1:]
              else:
                stek = stek[1:]
            else:
              finishSTR += "КП" + " "
              stek = stek[1:]
              if not("W27" in stek):
                checkPROC = False
              checkPROC1 -= 1
              checkPROC1 -= 2
              break
        elif i == "W5" and checkIF11:
          print("afafafaf")
          print(peremenay)
          continue
        elif i == "W5":
          print("ololololol")
          print(peremenay)
          
          for j in stek:
            if j != "W4":
              
              finishSTR += j + " "
              stek = stek[1:]
              
            else:
              stek = stek[1:]
              break
        elif i == "W13":  
          if "W4" == checkSTR[peremenay]:
            checkIF11 = True
          else:
            checkIF12 = True           
          for j in stek:
            if j != "W12":
              finishSTR += j + " "
              stek = stek[1:]
            else:
              finishSTR += "M1 УПЛ "
              stek[0] = stek[0] + " M1"
              break
        elif i == "R2" and checkMainVar:
          finishSTR += str(checkMainVar1) + " "
          checkMainVar1 = 0
        elif i == "R2" and checkVAR1:
          finishSTR += str(checkVAR) + " "
          checkVAR = 0
        
        elif i == "R3" and checkPROC:
          checkVAR = 0
          checkVAR1 = True
          finishSTR +=  str(checkPROC1) + " " + str(checkPROC2) + " " + "НП "
        elif i == "R4" and checkPROC:
          checkVAR = 0
          checkVAR1 = False
          finishSTR += "КО" + " " 
        
        elif i == "R3" or i == "W4":
          stek = [i] + stek
        elif i == "R4":
          
          for j in stek:
            if j != "R3" and j != "Ф":
              finishSTR += j + " "
              stek = stek[1:]
            elif j=="R3":
              stek = stek[1:]
              break
            elif j == "Ф":
              finishSTR += str(checkFunc+1) + " " + j + " "
              stek = stek[1:]
              checkFunc = 0
              break
        elif len(stek) == 0:
          stek.append(i)
        elif StekPriority[stek[0]]>=StekPriority[i]:
          
          for j in stek:
            if StekPriority[stek[0]]>=StekPriority[i]:
              if j != "R3" and j != "R4":
                finishSTR += j + " "
              stek = stek[1:]
            else:
              break
          if j != "R3" and j != "R4":
            stek = [i] + stek
        
        else:
          
          stek = [i] + stek
      elif i == "W6":
        checkMainVar = True

      elif i == "R6":
        checkMass = 2
        stek = ["АЭМ"] + stek
      elif (i == "R0") and ("W18" in stek):
        finishSTR += stek[0] + " "
        stek = stek[1:]
      elif (checkSTR.index(i) < (len(checkSTR)-1)) and i == "R0" and checkIF12 and checkSTR[peremenay] != "W14":
        for j in stek:
          if not("W12" in j):
            finishSTR += j + " "
            stek = stek[1:]
          else:
            finishSTR += "M1: "
            stek = stek[1:]
            checkIF12 = False
            break
      
      elif i == "R0" and checkIF1:
        
        for j in stek:
          if not("W12" in j):
            finishSTR += j + " "
            stek = stek[1:]
          else:
            finishSTR += "M2: "
            stek = stek[1:]
            checkIF1 = False
            break
      elif i == "R0" and checkIF12 and (checkSTR.index(i) == (len(checkSTR)-1)):
        for j in stek:
          if not("W12" in j):
            finishSTR += j + " "
            stek = stek[1:]
          else:
            finishSTR += "M1: "
            stek = stek[1:]
            checkIF12 = False
            break

      elif i == "R0" and checkFOR1:
        for j in stek:
          if not("W12" in j):
            finishSTR += j + " "
            stek = stek[1:]
          else:
            finishSTR += "<пц><пц>1+:=M1 БП M2 "
            stek = stek[1:]
            checkFOR1 = False
            break
      
      
      elif i == "R0" and checkVAR1:
        checkVAR = 0
      elif i == "R0" and checkMainVar:
        checkMainVar1 = 0
      elif i == "R0":
        for j in stek:
          if j == "O1" or j == "O0" or j == "O2" or j == "O3" or j == "O11":
            finishSTR += j + " "
            stek = stek[1:]
          else:
            break
      elif i == "R1" and checkMainVar:
        continue
      elif i == "R1" and checkVAR1:
        continue
      elif i == "R1":
        for j in stek:
          if j != "АЭМ" and j != "Ф":
            finishSTR += j + " "
            stek = stek[1:]
          elif j=="АЭМ":
            checkMass += 1
            break
          elif j=="Ф":
            checkFunc+=1
            break
      elif i == "R7":
        for j in stek:
          if j != "АЭМ":
            
            finishSTR += j + " "
            stek = stek[1:]
          else:
            finishSTR += str(checkMass) + j + " "
            stek = stek[1:]
            checkMass = 0
            break
      elif i == "R5":
        finishSTR
      else:
        if checkMainVar:
          checkMainVar1+=1
        if checkVAR1:
          checkVAR+=1
        finishSTR += i + " "

    if len(stek) != 0:
      for i in stek:
        if i !=  "R3" and i != "R4":
          finishSTR += i + " "
      
      stek = []
      

    
    return finishSTR.replace("W18","БП")


