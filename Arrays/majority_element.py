def majority_element(arr):
    for i in range(0,len(arr)):
        c=1
        for j in range(i+1,len(arr)):
            if(arr[i]==arr[j]):
                c+=1
        if c>len(arr)/2:
            return i
    return -1

if __name__=="__main__":
    print(majority_element([8,7,6,8,6,6,6,6]))