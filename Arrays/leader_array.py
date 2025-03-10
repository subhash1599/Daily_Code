def leader_array_brute_force(arr):
    for i in range(len(arr)):
        flag=False
        for j in range(i+1,len(arr)):
            if(arr[i]<=arr[j]):
                flag=True 
                break
        if flag==False:
            print(arr[i])
        




if __name__=="__main__":
    leader_array([7,10,4,3,6,5,2])



