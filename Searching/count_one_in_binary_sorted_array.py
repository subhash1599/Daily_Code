def count_one_binary_sorted_array(arr):
    count=0
    for i in range(len(arr)):
        if arr[i]==1:
            count+=1
    return count

def count_one_binary_sorted_array_efficient(arr):
    n=len(arr)
    low,high=0,n-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]==0):
            low=mid+1
        else:
            if(mid==0 or arr[mid-1]==0):
                return (n-mid)
            else:
                high=mid-1
    return 0

if __name__=="__main__":
    arr=[0,0,0,0,1,1,1,1]
    print(count_one_binary_sorted_array(arr))
    print(count_one_binary_sorted_array_efficient(arr))