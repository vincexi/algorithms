# In mathematics, the Fibonacci numbers, commonly denoted Fn, form a sequence, 
# called the Fibonacci sequence, such that each number is the sum of the two 
# preceding ones. 0 1 1 2 3 5 8

def getNthFib(n):
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1
	
    arr = [1, 1]
    for i in range(3,n):
        temp = arr[0] + arr[1]
        arr[0] = arr[1]
        arr[1] = temp
    return arr[1]

