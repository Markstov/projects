import translator as tr
import gui 
import OPZ
import assemblerTR as astr

analyzeTEXT = ""
finishSTR = ""

def changer_text(mass):
  global analyzeTEXT
  finish_text = ""
  
  for i in mass:
    checker = tr.func_main(i, '')
      
    if type(checker) == type("213"):
      finish_text +=checker+'\n'
    else:
      finish_text = "ERROR!"

  analyzeTEXT = finish_text.replace("\n"," ")
  return finish_text

def take_OPZ():
  global analyzeTEXT
  global finishSTR
  if analyzeTEXT != "":
    finishSTR = OPZ.opz(analyzeTEXT)
    return finishSTR
  else:
    return "...input text"

def assemb_trans():
  global finishSTR
  return astr.assemb_tr(finishSTR)
