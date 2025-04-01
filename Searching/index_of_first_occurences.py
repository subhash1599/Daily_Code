def first_occurence_naive(arr,key):
    for i in range(len(arr)):
        if(arr[i]==key):
            return i
    return -1


def first_occurence_efficient(arr,key):
    low,high=0,len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]>key):
            high=mid-1
        elif(arr[mid]<key):
            low=mid+1
        else:
            if(mid==0 or arr[mid-1]!=arr[mid]):
                return mid
            else:
                high=mid-1
    return -1

if __name__ == "__main__":
    arr=[1,10,10,10,20,20,40]
    key=5
    print(first_occurence_naive(arr,key))
    arr=[5,10,10,15,20,20,20]
    key=20
    print(first_occurence_efficient(arr,key))