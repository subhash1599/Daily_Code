def even_odd_subarray(arr):
    res=1
    for i in range(len(arr)):
        c=1
        for j in range(i+1,len(arr)):
            if (arr[j]%2==0 and arr[j-1]%2!=0) or (arr[j]%2!=0 and arr[j-1]%2==0):
                c+=1
            else:
                break 
        res=max(res,c)
    return res

if __name__=="__main__":
    print(even_odd_subarray([10,12,14,7,8]))
    print(even_odd_subarray([5,10,20,6,3,8]))

