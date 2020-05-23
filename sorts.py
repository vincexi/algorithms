# This sorting algorithm is comparison-based algorithm in which each pair of 
# adjacent elements is compared and the elements are swapped if they are not 
# in order. This algorithm is not suitable for large data sets as its average 
# and worst case complexity are of Ο(n2) where n is the number of items.
# https://www.tutorialspoint.com/data_structures_algorithms/bubble_sort_algorithm.htm

def bubbleSort(array):
    count = 1
    while count != 0:
        count = 0
        for idx, i in enumerate(array):
            nextNum = idx+1
            if idx+1 <= len(array) - 1 and i > array[nextNum]:
                array[idx], array[nextNum] = array[nextNum], array[idx]
                count += 1
    return array

# The array is searched sequentially and unsorted items are moved and inserted into 
# the sorted sub-list (in the same array). This algorithm is not suitable for large 
# data sets as its average and worst case complexity are of Ο(n2), where n is the number of items.
# https://www.tutorialspoint.com/data_structures_algorithms/insertion_sort_algorithm.htm

def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array

# Selection sort is a simple sorting algorithm. This sorting algorithm is an in-place 
# comparison-based algorithm in which the list is divided into two parts, the sorted 
# part at the left end and the unsorted part at the right end. Initially, the sorted 
# part is empty and the unsorted part is the entire list.

# The smallest element is selected from the unsorted array and swapped with the leftmost 
# element, and that element becomes a part of the sorted array. This process continues 
# moving unsorted array boundary by one element to the right.

# This algorithm is not suitable for large data sets as its average and worst case 
# complexities are of Ο(n2), where n is the number of items.

# https://www.tutorialspoint.com/data_structures_algorithms/selection_sort_algorithm.htm

def selectionSort(array):
    for idx, i in enumerate(array):
        j = idx+1
        for nextValue in range(j, len(array)):
            if array[nextValue] < array[idx]:
                array[idx], array[nextValue] = array[nextValue], array[idx]
    return array