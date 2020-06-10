def resheto(n):
    lst = [i for i in range(n + 1) if i % 2 != 0]
    lst.insert(1, 2)
    for i in lst:
        if i == 1 or i == 2: continue
        elif i ** 2 <= lst[-1]:
            for j in range(i ** 2, lst[-1], i):
                if j in lst: lst.remove(j)
        else: break
    del lst[0]
    return lst

file = open('input.txt' ,'r')
n = int(file.readline())
message = file.readline()
lst = resheto(len(message))
for i in range(n):
    res = ''
    s1 = message[:len(lst)]
    s2 = message[len(lst):]
    for k in range(1,len(message)+1):
        if k in lst:
            res += s1[0]
            s1 = s1[1:]
        else:
            res += s2[0]
            s2 = s2[1:]
    message = res
print(message)
output = open('output.txt', 'w')
output.write(message)
output.close()