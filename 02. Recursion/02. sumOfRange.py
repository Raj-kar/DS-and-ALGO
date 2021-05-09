def sumOfRange(num):
    if num == 1: return 1
    return num + sumOfRange(num - 1)

print(sumOfRange(1))
print(sumOfRange(3))
print(sumOfRange(5))
print(sumOfRange(10))