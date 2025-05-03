import tkinter

# function with unlimited arguments
def my_add(*args):
    ret = 0;
    for n in args:
        ret += n;
    return ret

print(f'addition: {my_add(1,2,3)}');
print(f'addition: {my_add(2,3)}');

def calculator(n, **kw):
    ret = 0
    ret += n + kw.get("add")
    ret += n * kw.get("mul")
    return ret

print(calculator(4, add=4, mul=5))
