def subarray_with_given_sum(arr,k):
    n=len(arr)
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum+=arr[j]
            if sum==k:
                return True
    return False


def subarray_with_given_sum_sliding_window(arr,k):
    curr,s=0,0
    n=len(arr)
    for e in range(n):
        curr+=arr[e]
        while(k<curr):
            curr-=arr[s]
            s+=1
        if curr==k:
            return True
    return False 


if __name__=="__main__":
    print(subarray_with_given_sum([1,4,20,3,10,5],33))
    print(subarray_with_given_sum([1,4,0,0,3,10,5],7))
    print(subarray_with_given_sum([2,4],3))
    print(subarray_with_given_sum_sliding_window([4,8,12,5],17))