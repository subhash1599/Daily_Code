def maximum_sum_subarray(arr,k):
    n=len(arr)
    res=arr[0]
    for i in range(n-k+1):
        curr=0
        for j in range(k):
            curr+=arr[i+j]
        res=max(res,curr)   
    return res



def maximum_sum_subarray_efficient(arr,k):
    curr=0
    for i in range(k):
        curr+=arr[i]
    res=curr
    for i in range(k,len(arr)):
        curr+=arr[i]-arr[i-k]
        res=max(res,curr)
    return res

'''
sliding window technique i have used in my second function where it will calculate the sum of first k elements and store it in a variable curr
then it will iterate from k to n and add the next element and subtract the first element of the window and then compare the sum with the previous sum
and store the maximum sum in res variable and return it at the end
Time complexity: O(n)
Space complexity: O(1)
'''




if __name__=="__main__":
    print(maximum_sum_subarray([10,5,-2,20,1],3))
    print(maximum_sum_subarray_efficient([1,8,30,-5,20,7],4))