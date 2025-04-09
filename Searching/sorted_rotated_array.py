def sorted_rotated_array(arr,key):
    for i in range(len(arr)):
        if(arr[i]==key):
            return i    
    return -1

if __name__=="__main__":
    arr=[100,200,400,1000,10,20]
    print(sorted_rotated_array(arr,10))
    
    