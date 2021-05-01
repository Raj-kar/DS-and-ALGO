import time


def monitorTime(func):
    """monitor total times take a function to get execute"""
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        total = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(round(end_time - start_time, 2), "sec")
        return total
    return wrapper

# Iterative method !
# Time complexity - O(n)
@monitorTime
def addUpTo(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total


print(addUpTo(99999999))


# Using Formula.
# Time complexity - O(1)
@monitorTime
def addUpTo(n):
    return n*(n+1) // 2


print(addUpTo(99999999))
