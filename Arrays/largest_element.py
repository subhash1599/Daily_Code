def largest_element(arr):
    if(len(arr)==0):
        return None
    
    result=arr[0]
    for i in range(len(arr)):
        if(arr[i]>result):
            result=arr[i]
    return result

if __name__=="__main__":
    arr=[1,90,34,2,190,89]
    print(largest_element(arr))