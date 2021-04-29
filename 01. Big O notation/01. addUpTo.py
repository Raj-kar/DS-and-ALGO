# Iterative method !
# Time complexity - O(n)
def addUpTo(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total


print(addUpTo(10))


# Using Formula.
# Time complexity - O(1)
def addUpTo(n):
    return n*(n+1) // 2


print(addUpTo(10))
