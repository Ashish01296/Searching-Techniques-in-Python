#Linear Search

def linear_search(arr, size, key):
    for i in range(size):
        if arr[i] == key:
            return i
    return -1
    
    
    
c = [1,3,5,7,9,11]

b = linear_search(c,6,11)

print("The element at index number is: ",b)



#output
The element at index number is:  5
