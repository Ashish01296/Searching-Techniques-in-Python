def first_occurrence(arr, key):
    start = 0
    end = len(arr) - 1
    ans = -1

    while start <= end:
        mid = int(start + (end - start) // 2)

        if arr[mid] == key:
            ans = mid
            end = mid - 1
        elif key > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return ans


def last_occurrence(arr, key):
    start = 0
    end = len(arr) - 1
    ans = -1

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == key:
            ans = mid
            start = mid + 1
        elif key > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return ans



odd = [0, 5, 5, 6, 7, 6, 8]
    
print("First occurrence of 6:", first_occurrence(odd, 6))
print("Last occurrence of 6:", last_occurrence(odd, 6))



b = (last_occurrence(odd,6) - first_occurrence(odd,6))

print("The Element 6 number of occurence is",b)



#output
The Element 6 number of occurence is 2

