def prefix_sum(arr):
    n=len(arr)
    prefix=[0]*n 
    prefix[0]=arr[0]

    for i in range(1,n):
        prefix[i]=prefix[i-1]+arr[i]
    return prefix

def range_sum(prefix,L,R):
    if L==0:
        return prefix[R]    
    
    return prefix[R]-prefix[L-1]


if __name__=="__main__":
    arr = [3, 6, 2, 8, 7, 4, 5]
    prefix=prefix_sum(arr)
    queries = [(1, 3), (2, 5)]  
    for L, R in queries:
        print(range_sum(prefix, L, R))  #