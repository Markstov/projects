import math

def check(strok):
    t = False
    coun = 0
    for i in range(len(strok))[::-1]:
        t = True if strok[i] == '1' or t else False
        coun = coun + 1 if strok[i] == '1' else coun
        if t and strok[i] == '0':
            return strok[:i] + '1' + ''.join(['0' for i in range (len(strok) - i - coun)]) +''.join(['1' for i in range(coun - 1)])
            
def apmask(strok, mask):
    return ''.join([(strok[i] if mask[i] == '0' else ('t' if strok[i] == 'f' else 'f')) for i in range(len(strok))])

lines = [line.split('\n')[0] for line in open('input.txt', 'r').readlines() if len(line) > 3]
variants = {}
for line in lines:
    variants[line[:-1]] = [abs(int(line[-1]) - ((len(line)) // 2)), int(line[-1])] #?
triedVariants = variants.keys()
variants = sorted(variants.items(), key=lambda kv: kv[1], reverse=True)

onesAmount = len(variants[0][0]) - variants[0][1][1]
zerosAmount = variants[0][1][1]

strok = ''.join(['0' for i in range(zerosAmount)]) + ''.join(['1' for i in range(onesAmount)])

posSolutionAmount = 0
posSolution = []

nSolution = apmask(variants[0][0], strok)
if not nSolution in triedVariants:
    posSolution.append(nSolution)
    posSolutionAmount += 1
for i in range(int(math.factorial(len(strok)) / (math.factorial(zerosAmount)*math.factorial(onesAmount))) - 1):
    strok = check(strok)
    nSolution = apmask(variants[0][0], strok)
    if not nSolution in triedVariants:
        posSolution.append(nSolution)
        posSolutionAmount += 1
output = 'ONE SOLUTION' if posSolutionAmount == 1 else 'POSSIBLE SOLUTION'
output = output + '\n' + ''.join([solution + '\n' for solution in posSolution])
output = output[:-1]
open('output.txt', 'w').write(output)
print(output)