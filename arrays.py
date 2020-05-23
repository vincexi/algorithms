# An array is called monotonic if it is either monotone increasing or monotone decreasing.

def isMonotonic(array):
    increasing = 0
    for idx, i in enumerate(array):
        if idx+1 < len(array):
            if i < array[idx+1]:
                increasing += 1
    return True if increasing == len(array) - 1 or increasing == 0 else False


# Find the three largest numbers in an array

def findThreeLargestNumbers(array):
    largest, second, third = float('-inf'), float('-inf'), float('-inf')
	
    for i in array:
        if i >= largest:
            third = second
            second = largest
            largest = i
        elif i >= second:
            third = second
            second = i
        elif i >= third:
            third = i
	
    return [third, second, largest]
