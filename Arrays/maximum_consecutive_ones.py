def maximum_consecutive_ones_naive(arr):
    res=0
    for i in range(len(arr)):
        curr=0
        for j in range(i,len(arr)):
            if arr[j]==1: curr+=1
            else: break
        res=max(curr,res)
    return res    
            
    
    
def maximum_consecutive_ones_efficient(arr):
    res,curr=0,0
    for i in range(len(arr)):
        if arr[i]==0: curr=0
        else: curr+=1; res=max(res,curr)
    return res



if __name__=="__main__":
    print(maximum_consecutive_ones_naive([0,1,1,0,1,0]))
    print(maximum_consecutive_ones_naive([0,1,1,1,0,1,1]))
    print(maximum_consecutive_ones_efficient([0,1,1,1,0,1,1]))
    print(maximum_consecutive_ones_efficient([0,1,1,0,1,1,1]))