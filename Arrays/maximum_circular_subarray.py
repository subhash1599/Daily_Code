def max_circular_subarray(arr):
    res=arr[0]
    for i in range(len(arr)):
        curr_max=arr[i]
        curr_sum=arr[i]
        for j in range(1,len(arr)):
            index=(i+j)%(len(arr)) #when we exceed the array length then will wrap around to the beginning
            curr_sum+=arr[index]
            curr_max=max(curr_max,curr_sum)
        res=max(res,curr_max)
    return res


def normal_max_subarray(arr):
    res=arr[0]
    maxEnding=arr[0]
    for i in range(len(arr)):
        maxEnding=max(maxEnding+arr[i],arr[i])
        res=max(maxEnding,res)
    return res

def overall_max_subarray(arr):
    max_normal=normal_max_subarray(arr)
    if(max_normal<0):
        return max_normal
    arr_sum=0
    for i in range(len(arr)):
        arr_sum+=arr[i]
        arr[i]-=arr[i]
    max_circular=arr_sum+normal_max_subarray(arr)
    return max(max_normal,max_circular)


if __name__=="__main__":
    print(max_circular_subarray([5,-2,3,4]))
    print(overall_max_subarray([8,-4,3,-5,4]))