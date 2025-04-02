def index_of_last_ocuurences(arr,key):
    for i in range(len(arr)-1,-1,-1):
        if(arr[i]==key):
            return i
    return -1


def index_of_last_ocuurences_efficient(arr,key):
    low,high=0,len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]>key):
            high=mid-1
        elif(arr[mid]<key):
            low=mid+1
        else:
            if(mid==len(arr)-1 or arr[mid+1]!=arr[mid]):
                return mid
            else:
                low=mid+1
    return -1


if __name__ == "__main__":
    arr=[1,10,10,10,20,20,40]
    key=5
    print(index_of_last_ocuurences(arr,key))
    arr=[5,10,10,15,20,20,20]
    key=20
    print(index_of_last_ocuurences_efficient(arr,key))