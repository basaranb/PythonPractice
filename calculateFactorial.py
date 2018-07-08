#recursive factorial
def factorial(i):
    if i == 0:
        return 1
    return i*factorial(i-1)
x=int(raw_input())
print(factorial(x))


#non-recursive factorial
def facto(i):
    if i == 0:
        return 1
    else:
        a=1
        for i in range(1,i+1):
            a=i*a
        return a
y=int(raw_input())
print (facto(y))
