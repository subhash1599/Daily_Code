def array_is_sort(arr):
    res=True
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            res=False
    return res 

if __name__=="__main__":
    print(array_is_sort([1,4,89]))