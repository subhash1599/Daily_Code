def frequency_sorted_array(arr):
    freq=1
    n=len(arr)
    for i in range(1,n):
        if(arr[i]==arr[i-1]):
            freq+=1
            
        else:
            print(arr[i-1],freq)
            freq=1
    print(arr[-1],freq)
    
    
if __name__=="__main__":
    print(frequency_sorted_array([40,50,50,50]))
                