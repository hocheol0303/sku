def func1(t):
    return t()
def func2():
    return 'hihi'


print(func1(func2))

a=[3,2,1]

print(sorted(a))
a.sort()
print(a)