# Shell Sort Algorithm

# ShellSort implementation
def shellSort(alist):
    sublistCount = len(alist) // 2
    while sublistCount > 0:
        # sublistCount = sublistCount // 2

        for startPosition in range(sublistCount):
            gapInsertionSort(alist, startPosition, sublistCount)

        print("After increments of size ", sublistCount, "The list is ", alist)

        sublistCount = sublistCount // 2



def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):

        currentValue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentValue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentValue


alist = [54, 26, 93, 17, 77, 31, 44, 20, 55]

shellSort(alist)
print(alist)