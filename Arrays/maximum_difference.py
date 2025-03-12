def maximum_difference_bruteforce(arr):
    res=arr[1]-arr[0]
    temp=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            temp=arr[j]-arr[i]
            res=max(temp,res)
    return res 



def maximum_difference_efficient(arr):
    res=arr[1]-arr[0]
    minVal=arr[0]
    for j in range(1,len(arr)):
        res=max(res,arr[j]-minVal)
        minVal=min(minVal,arr[j])
    return res

if __name__=="__main__":
    print(maximum_difference_bruteforce([30,10,8,2]))
    print(maximum_difference_efficient([2,3,10,6,4,8,1]))
                
                

# whenever we are using min and max inbuilt functions with two arguments then the time complexity of it is O(1).
# Incase if we are using any iterable i mean list then time complexity is O(n).