def fact(num):
    if num == 1: return 1
    return num * fact(num - 1)

print(fact(5))
print(fact(4))
print(fact(1))