# Insertion Sort Algorithm

def insertionSort(alist):
    for index in range(1, len(alist)):
        currentValue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentValue:
            alist[position] = alist[position - 1]
            position = position - 1

        alist[position] = currentValue

alist = [54, -26, 93, 77, 31, 44, -55, -20]
insertionSort(alist)
print(alist)