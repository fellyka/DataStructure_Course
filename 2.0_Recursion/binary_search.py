def binarySearch(data, target, low, high):
    mid = (low + high)//2
    if low > high:
        return False
    if target == data[mid]:
        return True
    elif target < data[mid]:
        return binarySearch(data, target, low, high-1)
    else:
        return binarySearch(data, target, low+1, high)


# Applying the binarySearch function

listA = [22, 29, 33, 37, 56, 85, 101, 248, 278, 278, 299, 301, 302, 305, 386, 444, 456, 489, 499, 508, 579, 599, 1000, 1001, 1056, 1061]
target = 278
valueFound = binarySearch(listA, target,0,len(listA) - 1)  

if(valueFound):
    print(f"{target} is found at index {listA.index(target)}")
else:
    print(f"{target} missing from the list")