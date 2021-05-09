# Collect of the odd values in an array.

def collectOddValues(arr):
    result = []

    def helper(arr):
        if len(arr) <= 0:
            return
        if arr[0] % 2 != 0:
            result.append(arr[0])

        arr.pop(0)

        helper(arr)

    helper(arr)
    return result


print(collectOddValues([11, 22, 4131, 1246, 9984, 3525]))
print(collectOddValues([3, 21, 531, 316, 984, 125]))
