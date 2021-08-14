import random

def func(n):

    arr = []
    sizes = []
    i = 0
    flag = False

    while i < n:

        randSize = random.randrange(0, 10)

        for size in sizes:
            if randSize == size:
                flag = True

        if not flag:
            arr.append([])
            sizes.append(randSize)
            for j in range(randSize):
                arr[i].append(random.randrange(0, 15))
            i+=1

        flag = False

    for row in arr:
        index = arr.index(row)
        if index % 2 == 0:
            arr[index].sort()
        else:
            arr[index].sort(reverse = True)

    return arr
  
n = int(input("Значение n "))
print(func(n))

