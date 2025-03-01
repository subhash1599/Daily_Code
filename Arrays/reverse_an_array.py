def reverse_an_array(arr):
    low=0
    high=len(arr)-1
    print(high)
    while(low<high):
        temp=arr[low]
        arr[low]=arr[high]
        arr[high]=temp
        low=low+1
        high=high-1
    return arr 

if __name__=="__main__":
    print(reverse_an_array([1,2,3,4]))