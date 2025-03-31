def binary_search(arr,key):
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



def binary_search_recursive(arr,key,low,high):
    if(low>high):
        return -1
    mid=(low+high)//2
    if(arr[mid]>key):
        return binary_search_recursive(arr,key,low,mid-1)
    elif(arr[mid]<key):
        return binary_search_recursive(arr,key,mid+1,high)
    else:
        return mid


if __name__=="__main__":
    arr=[10,20,30,40,50,60,70]
    print(binary_search(arr,60))
    print(binary_search_recursive(  arr,20,0,len(arr)-1))