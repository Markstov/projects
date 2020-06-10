def transposition(strok): 
  for i in range(len(strok)):
    if strok.count(chr(65+i)) != 1:
      return False
  return True  

def almost_transposition(strok, n): 
  if len(strok) - n != 1:
    return False
  for i in range(len(strok)):
    if transposition(strok[:i]+strok[i+1:]):
      return True
  return False

def hyper_almost_transposition(strok, n):   
  if len(strok) < n + 1:
    return False
  for i in range(len(strok)-n):
    if not almost_transposition(strok[i:i+n+1], n):
      return False
  return True
  
def builder(strok, part): 
  if part < 0:
    strok = chr(65) + strok 
  else:
    if ord(strok[part]) + 1 < 65 + n:
      strok = strok[:part] + chr(ord(strok[part]) + 1) + strok[part + 1:]
    else:
      strok = builder(strok[:part] + chr(65) + strok[part + 1:], part - 1)
  return strok

file = open('input.txt', 'r').readlines()
n = int(file[0].split('\n')[0])
strok1 = file[1].split('\n')[0]
strok2 = file[2].split('\n')[0]

strok = max(strok1, strok2)
while not(hyper_almost_transposition(strok, n) and (strok1 in strok) and (strok2 in strok)):
  strok = builder(strok, len(strok) - 1)

print(strok)

open('output.txt', 'w').write(strok)