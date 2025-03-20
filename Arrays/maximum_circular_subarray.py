def max_circular_subarray(arr):
    res=arr[0]
    for i in range(len(arr)):
        curr_max=arr[i]
        curr_sum=arr[i]
        for j in range(1,len(arr)):
            index=(i+j)%(len(arr))
            curr_sum+=arr[index]
            curr_max=max(curr_max,curr_sum)
        res=max(res,curr_max)
    return res
if __name__=="__main__":
    print(max_circular_subarray([5,-2,3,4]))