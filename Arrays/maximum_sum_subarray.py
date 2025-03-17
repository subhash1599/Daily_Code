def max_sum_subarray_naive(arr):
    res=arr[0]
    for i in range(len(arr)):
        curr=0
        for j in range(i,len(arr)):
            curr+=arr[j]
            res=max(res,curr)
    return res


def max_sum_subarray_efficient(arr):
    res=arr[0]
    maxEnding=arr[0]
    for i in range(1,len(arr)):
        maxEnding=max(maxEnding+arr[i],arr[i])
        res=max(maxEnding,res)
    return res
if __name__=="__main__":
    print(max_sum_subarray_naive([1,-2,3,-1,2]))
    print(max_sum_subarray_efficient([-3,8,-2,4,-5,6]))


