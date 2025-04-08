def infinite_array_search(arr,key):
    i=0
    while(True):
        if(arr[i]==key):
            return i
        elif(arr[i]>key):
            return -1
        i+=1

def infinite_array_search_efficient(arr,key):
    if(arr[0]==key): return key
    i=1
    while(arr[i]<key):
        i*=2
    low,high=i//2,i
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]==key):
            return mid
        elif(arr[mid]<key):
            low=mid+1
        else:
            high=mid-1
    return -1


if __name__ == "__main__":
    print(infinite_array_search([1,10,200],15))
    print(infinite_array_search_efficient([1,10,15,20,40,60,80,100,200,500,1000],100))

    