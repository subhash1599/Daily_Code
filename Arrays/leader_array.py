def leader_array_brute_force(arr):
    for i in range(len(arr)):
        flag=False
        for j in range(i+1,len(arr)):
            if(arr[i]<=arr[j]):
                flag=True 
                break
        if flag==False:
            print(arr[i])
        

def leader_array_efficient(arr):
    n=len(arr)
    curr_ladder=arr[n-1]
    print(curr_ladder)
    for i in range(n-2,-1,-1):
        if(curr_ladder<arr[i]):
            curr_ladder=arr[i]
            print(curr_ladder,"curr")


if __name__=="__main__":
    leader_array_brute_force([7,10,4,3,6,5,2])
    leader_array_efficient([7,10,4,3,6,5,2])




