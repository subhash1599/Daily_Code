def sorted_rotated_array(arr,key):
    for i in range(len(arr)):
        if(arr[i]==key):
            return i    
    return -1

def sorted_rotated_array_efficient(arr,key):
    low,high=0,len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]==key):
            return mid
        if(arr[low]<=arr[mid]):
            if(key>=arr[low] and key<=arr[mid]):
                high=mid-1
            else:
                low=mid+1
        else:
            if(key>=arr[mid] and key<=arr[high]):
                low=mid+1
            else:
                high=mid-1
    return -1

if __name__=="__main__":
    arr=[100,200,400,1000,10,20]
    print(sorted_rotated_array(arr,10))
    arr=[10,20,40,60,5,8]
    print(sorted_rotated_array_efficient(arr,5))
    