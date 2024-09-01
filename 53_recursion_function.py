# #A function calling  itself
# def count_down(n):
#     print(n)
#     if n==0:
#         return
#     else:
#         n=count_down(n-1)

# count_down(1000)

#maximum recursion depth

import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(10000)
def count_down(n):
    print(n)
    if n==0:
        return
    else:
        n=count_down(n-1)

count_down(99)


