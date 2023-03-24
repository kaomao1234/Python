def mergeSort(arr:list,left:int,right:int):
    if left < right:
        mid = (left + right)//2
        mergeSort(arr,left,mid)
        mergeSort(arr,mid+1,right)
        merge(arr,left,mid,right)
def merge(arr:list,left:int,mid:int,right:int):
    lenLeft = mid - left + 1
    lenRight = right - mid
    tempLeft = [0] * lenLeft
    tempRight = [0] * lenRight
    for i in range(lenLeft):
        tempLeft[i] = arr[left + i]
    for j in range(lenRight):
        tempRight[j] = arr[mid + j + 1]
    i = 0
    j = 0
    k = left
    while i < lenLeft and j < lenRight:
        if tempLeft[i] <= tempRight[j]:
            arr[k] = tempLeft[i]
            i += 1
        else:
            arr[k] = tempRight[j]
            j += 1
        k += 1
    while i < lenLeft:
        arr[k] = tempLeft[i]
        i += 1
        k += 1
    while j < lenRight:
        arr[k] = tempRight[j]
        j += 1
        k += 1

array = [9,5,7,4,2,8]
mergeSort(array,0,len(array)-1)
print(array)