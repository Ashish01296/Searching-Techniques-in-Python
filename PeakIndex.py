#Peak Index Mountain..

def peakindex(arr):

    low = 0
    high = len(arr) -1
    mid = int(low + (high-low)/2)

    while low<high:
        if(arr[mid]<arr[mid+1]):
            low = mid + 1
        else:
            high = mid
        mid = int(low +(high-low)/2)

    return low






num = [0,2,1,0]

print(peakindex(num))



#output 

#1
        

