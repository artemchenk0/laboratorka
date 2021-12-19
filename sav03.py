import random

ch = 10
a = []
for i in range(0, ch):
    a.append(random.randint(0, 1000))
print(a)
s = 0
p = 0
for i in range(0, len(a) - 1):
    for j in range(0, len(a) - 1):
        s += 1
        if a[j] > a[j+1]:
            a[j + 1], a[j] = a[j], a[j + 1]
            p += 1
print(a)
print('сравнения:', s)
print('перестановки: ', p)
print("...................................................................")


print("метод пузырьком частично", ch)
a = []
for i in range(0, ch):
    a.append(random.randint(0, 1000))
print(a)

s = 0
p = 0
for i in range(0, len(a) - 1):
    for j in range(0, len(a) - 1):
        s += 1
        if a[j] > a[j + 1]:
            a[j + 1], a[j] = a[j], a[j + 1]
            p += 1
print('сравнение:', s)
print('перестановки:', p)
print(".....................................................................")

print("Пузырьком", ch)
a = []
for i in range(0, ch):
    a.append(random.randint(0, 1000))
print(a)
a.sort()
print(a)
s = 0
p = 0
for i in range(0, len(a) - 1):
    for j in range(0, len(a) - 1):
        s += 1
        if a[j] > a[j + 1]:
            a[j + 1], a[j] = a[j], a[j + 1]
            p += 1
print(a)
print('сравнения:', s)
print('перестановки:', p)
print("...................................................................")


print("метод вставками несортированный", ch)
a = []
for i in range(0, ch):
    a.append(random.randint(0,1000))
print(a)
s = 0
p = 0
for i in range(1, len(a)):
    for j in range(i, 0, -1):
        s += 1
        if a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            p += 1
        else:
            break
print(a)
print('сравнения:', s)
print('перестановки:', p)
print("..................................................................")


print("вставками частично", ch)
a = []
for i in range(0, ch):
    a.append(random.randint(0,1000))
print(a)
for j in range(0, (len(a) // 2)):
    for j in range(0, (len(a) // 2)):
        if a[j] > a[j + 1]:
            a[j + 1], a[j] = a[j], a[j + 1]
print(a)
s = 0
p = 0
for i in range(1, len(a)):
    for j in range(i, 0, -1):
        s += 1
        if a[j] < a[j-1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            p += 1
        else:
            break
print(a)
print('сравнения:', s)
print('перестановки:', p)
print("........................................................................")


print("вставками сортированный", ch)
a = []
for i in range(0, ch):
    a.append(random.randint(0, 1000))
print(a)
a.sort()
print(a)
s = 0
p = 0
for i in range(1, len(a)):
    for j in range(i, 0, -1):
        s += 1
        if a[j] < a[j-1]:
            a[j], a[j-1] = a[j - 1], a[j]
            p += 1
        else:
            break
print(a)
print('сравнения:', s)
print('перестановки:', p)
print(".........................................................................")


print("метод выбором несортированный", ch)
a = []
for i in range(0, ch):
    a.append(random.randint(0, 1000))
print(a)
s = 0
p = 0
for i in range(0, len(a)):
    minim = i
    for j in range(i + 1, len(a)):
        s += 1
        if a[j] < a[minim]:
            minim = j
    a[minim], a[i] = a[i], a[minim]
    p += 1
print(a)
print('сравнения:', s)
print('перестановки:', p)
print(".........................................................................")


print("выбором частично", ch)
a = []
for i in range(0, ch):
    a.append(random.randint(0, 1000))
print(a)
for j in range(0, (len(a) // 2)):
    for j in range(0, (len(a) // 2)):
        if a[j] > a[j + 1]:
            a[j + 1], a[j] = a[j], a[j + 1]
print(a)
s = 0
p = 0
for i in range(0, len(a)):
    minim = i
    for j in range(i + 1, len(a)):
        s += 1
        if a[j] < a[minim]:
            minim = j
    a[minim], a[i] = a[i], a[minim]
    p += 1
print(a)
print('сравнения:', s)
print('перестановки:', p)
print("..............................................................................")


print("выбором сортированный ", ch)
a = []
for i in range(0, ch):
    a.append(random.randint(0, 1000))
print(a)
a.sort()
print(a)
s=0
p=0
for i in range(0, len(a)):
    min = i
    for j in range(i + 1, len(a)):
        s += 1
        if a[j] < a[min]:
            min = j
    a[min], a[i] = a[i], a[min]
    p += 1
print(a)
print('сравнения:', s)
print('перестановки:', p)
print(".............................................................................")


print("шелла несортированный", ch)
a = []
for i in range(0, ch):
    a.append(random.randint(0, 1000))
print(a)
s = 0
p = 0
dp = len(a) // 2
while dp > 0:
    for i in range(dp, len(a)):
        cr = a[i]
        ps = i
        while ps >= dp and a[ps - dp] > cr:
            s += 1
            p += 1
            a[ps] = a[ps - dp]
            ps -= dp
            a[ps] = cr
    dp = dp // 2
print(a)
print('сравнения:', s)
print('перестановки:', p)
print(".............................................................................")


print("шелла частично сорт", ch)
a = []
for i in range(0, ch):
    a.append(random.randint(0, 1000))
print(a)
for j in range(0, (len(a) // 2)):
    for j in range(0, (len(a) // 2)):
        if a[j] > a[j + 1]:
            a[j + 1], a[j] = a[j], a[j + 1]
print(a)
s = 0
p = 0
dp = len(a) // 2
while dp > 0:
    for i in range(dp, len(a)):
        cr = a[i]
        ps = i
        while ps >= dp and a[ps - dp] > cr:
            s += 1
            p += 1
            a[ps] = a[ps - dp]
            ps -= dp
            a[ps] = cr
    dp = dp // 2
print(a)
print('сравнения:', s)
print('перестановки:', p)
print(".................................................................................")


print("шелла сортированный", ch)
a = []
for i in range(0, ch):
    a.append(random.randint(0, 1000))
print(a)
a.sort()
print(a)
s = 0
p = 0
dp = len(a) // 2
while dp > 0:
    for i in range(dp, len(a)):
        cr = a[i]
        ps = i
        while ps >= dp and a[ps - dp] > cr:
            s += 1
            p += 1
            a[ps] = a[ps - dp]
            ps -= dp
            a[ps] = cr
    dp = dp // 2
print(a)
print('сравнения: ', s)
print('перестановки: ', p)
print("...............................................................................")


def test(arr):
    global c_comp, c_swap
    c_comp, c_swap = 0, 0
    quick_sort(arr, 0, len(arr) - 1)


def quick_sort(x, ibeg, iend):
    global c_comp, c_swap
    if (iend - ibeg) <= 1:
        return
    isep = (ibeg + iend) // 2
    sep = x[isep]
    i = ibeg
    j = iend
    while True:
        while x[i] < sep:
            i += 1
            c_comp += 1
        while x[j] > sep:
            j -= 1
            c_comp += 1
        if i <= j:
            x[i], x[j] = x[j], x[i]
            c_swap += 1
            i += 1
            j -= 1
        if i >= j:
            break
    quick_sort(x, ibeg, j)
    quick_sort(x, i, iend)


print("КьюСорт сортированный", ch)
x = []

for i in range(0, ch):
    x.append(random.randint(0, 1000))
print(x)
test(x)
print(x)
print('сравнения: '+str(c_comp))
print('перестановки: '+str(c_swap))


print("КьюСорт частично", ch)
x = []
for i in range(0, ch):
    x.append(random.randint(0, 1000))
print(x)
for j in range(0, len(x) // 2):
    for j in range(0, len(x) // 2):
        if x[j] > x[j + 1]:
            x[j + 1], x[j] = x[j], x[j + 1]
print(x)
test(x)
print(x)
print('сравнения: '+str(c_comp))
print('перестановки: '+str(c_swap))
print("...........................................................................")


print("КьюСорт сорт", ch)
x = []
for i in range(0, ch):
    x.append(random.randint(0, 1000))
print(x)
x.sort()
print(x)
test(x)
print(x)
print('сравнения: ' + str(c_comp))
print('перестановки: ' + str(c_swap))