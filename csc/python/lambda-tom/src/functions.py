# how to define a function
# def someFunc(x):
#     return x
name = "dave"
l = [1, 2, 3, 4]

def cap(n):
    return n.capitalize()
# define a doubling function that passes args by value
def mult(x):
    return x * 2
# define a doubling function that passes args by reference

def mult2(lst):
    for i in range(len(lst)):
       # lst[i] = lst[i] * 2
       lst[i] *= 2
    # no return necessary -
    # passing by reference means that
    # original list is modified

# try out our functions
# var1 = someFunc("Hello") # => "Hello"
print(name) # => "dave"
cap(name) # => "Dave" pass by val
print(name) # => "dave"

# mult
n = 12
print(n)
print(mult(n))
print(n)

# mult2
print(l) # => [1, 2, 3, 4]
print(mult2(l)) # => None
print(l) # [2, 4, 6, 8]
