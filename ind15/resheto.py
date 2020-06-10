#Оптимизация №1. Сокращаем число операций(идем не по всем числам, а до того момента пока i^2 >= n)
#Оптимизация №2. Четные числа кроме 2 не являются простыми => их можно пропустить (вдвое сокращается память)
def reshetoEratosfena(n):
    lst = [i for i in range(n + 1) if i % 2 != 0]
    lst.insert(1, 2)
    for i in lst:
        if i == 1 or i == 2: continue
        elif i ** 2 <= lst[-1]:
            for j in range(i ** 2, lst[-1], i):
                if j in lst: lst.remove(j)
        else: break
    return lst

N = int(input("Input even number: "))
print(reshetoEratosfena(N))