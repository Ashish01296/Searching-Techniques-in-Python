# Binary Search in python


def binarySearch(array, x, low, high):

    #it will iterate the whole list and it will come out from while loop  when high>low 
    while low <= high:

        mid = int(low + (high - low)//2)

        if array[mid] == x:
            return mid

        elif (key>arr[mid]):
            low = mid + 1

        elif(key<arr[mid):
            high = mid - 1

    return -1


array = [2,4,6,8,9,10]
x = 9

result = binarySearch(array, x, 0, len(array)-1)

print("index is:",result)




#output is index is 4
