def collectOddValues(arr):
    newArr = []

    if (len(arr) == 0):
        return newArr

    if (arr[0] % 2 != 0):
        newArr.append(arr[0])

    arr.pop(0)
    newArr += collectOddValues(arr)
    return newArr


print(collectOddValues([11, 22, 4131, 1246, 9984, 3525]))
print(collectOddValues([3, 21, 531, 316, 984, 125]))
