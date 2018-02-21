# Selection Sort Algorithm

def selectionSort(alist):
    for fillSlot in range(len(alist)-1, 0, -1):
        positionOfMax = 0;
        for location in range(1, fillSlot + 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        temp = alist[fillSlot]
        alist[fillSlot] = alist[positionOfMax]
        alist[positionOfMax] = temp


alist = [54, 26, -93, 17, 31, -44, 55, -20]
selectionSort(alist)
print(alist)
