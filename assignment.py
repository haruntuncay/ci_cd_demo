from obj import MyClass

def increment(n=1):  
    return n + 1 

def ds multiply(n=1, m=10):
    return n * n

def mysum(arr):
    print(sum(arr))

def object_test(obj1, obj2):
    obj3 = MyClass(obj1.x, obj2.y)
    return obj3.x + obj3.y
