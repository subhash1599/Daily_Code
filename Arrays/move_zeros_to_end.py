def move_zeros_to_end_naive(arr):
    for i in range(len(arr)):
        if(arr[i]==0):
            for j in range(i+1,len(arr)):
                if(arr[j]!=0):
                    arr[i],arr[j]=arr[j],arr[i]
                    break 
    return arr

if __name__=="__main__":
    print(move_zeros_to_end_naive([8,5,0,10,0,20]))
    print(move_zeros_to_end_naive([10,5,0,0,8,0,9,0]))


def move_zeros_to_end_efficient(arr):
    count=0
    for i in range(len(arr)):
        if(arr[i]!=0):
            arr[i],arr[count]=arr[count],arr[i]
            count+=1
    return arr

if __name__=="__main__":
    print(move_zeros_to_end_efficient([8,5,0,10,0,20]))
