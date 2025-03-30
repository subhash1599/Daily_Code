def binary_seatch(arr,key):
    low,high=0,len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]>key):
            high=mid-1
        elif(arr[mid]<key):
            low=mid+1
        else:
            return mid
    return -1

if __name__=="__main__":
    arr=[10,20,30,40,50,60,70]
    print(binary_seatch(arr,60))