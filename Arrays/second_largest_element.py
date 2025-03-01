import largest_element 

def second_largest(arr):
    result=arr[0]
    largest=largest_element.largest_element(arr)
    for i in range(len(arr)):
        if (arr[i]> result) and (arr[i]!=largest):
            result=arr[i]
    return result

if __name__=="__main__":
    print(second_largest([1,90,3,72,22,39,80]))


#This above code is taking O(2n) time complexity

#This is very efficient approach
'''
Here in the second loop we are finding the second largest element 
'''
def second_largest_efficient(arr):
    res,largest=-1,0
    for i in range(1,len(arr)):
        print(arr[i])
        if(arr[i]>arr[largest]):
            res=largest
            print("res",res)
            largest=i
            print("largest",largest)
        elif(arr[i]!=arr[largest]):
            if(res==-1) or (arr[i]>arr[res]):
                res=i
                print("res_final",res)
    return res
    
if __name__=="__main__":
    print(second_largest_efficient([1,90,3,72,22,39,80]))