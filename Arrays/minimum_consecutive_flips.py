def min_flips(arr):
    n=len(arr)
    for i in range(1,n):
        if arr[i]!=arr[i-1]:
            if(arr[i]!=arr[0]):
                print(f"From {i} to ",end="")
            else:
                print(i-1)
    if(arr[n-1]!=arr[0]):
        print(n-1)

if __name__=="__main__":
    min_flips([0,0,1,1,0,0,1,1,0])