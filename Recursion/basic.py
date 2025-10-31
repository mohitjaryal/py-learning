# Basic demonstration of recursion in py
def show(n):
    if n == 0:
        return    # stop recursion
    else:
        print(n)
        show(n - 1)   # recursive call


show(4)