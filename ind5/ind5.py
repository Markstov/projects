def get_symbol_by_code(alp, code):
    for key, value in alp.items():
        if value == code:
            return key

alp = dict()
alp[' '] = 0
for i in range(1,27):
    alp[chr(64+i)] = i

file = open('input.txt')
lst = list()
for line in file:
    lst.append(line.replace("\n",""))

allwords = lst[1:len(lst)-1]
message = lst[len(lst)-1]
max = 0
resault = ""

for k in range(0,27):
    decoded = ""
    for symbol in message:
        new = get_symbol_by_code(alp, (alp[symbol] + k) % 27)
        decoded += new

    count = 0
    for word in decoded.split(" "):
        if word in allwords:
            count += 1
    if count > max:
        max = count
        resault = decoded

output_file = open('output.txt', 'w')
output_file.write(resault)
output_file.close()