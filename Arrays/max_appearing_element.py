def max_appearing_element(left,right,n):
    freq=[0]*100
    for i in range(n):
        for j in range(left[i],right[i]+1):
            freq[j]+=1
    
    res=0
    for i in range(1,100):
        if freq[i]>freq[res]:
            res=i

    return res


def max_appearing_element_efficient(left,right,n):
    freq=[0]*100
    for i in range(n):
        freq[left[i]]+=1
        freq[right[i]+1]-=1
    res=0
    maxFreq=freq[0]
    for i in range(1,100):
        freq[i]+=freq[i-1]
        if freq[i]>maxFreq:
            maxFreq=freq[i]
            res=i
    return res
       
    

if __name__ == '__main__':
    left=[1,2,4]
    right=[4,5,7]
    n=len(left)
    print(max_appearing_element(left,right,n))
    left=[1,2,5,15]
    right=[5,8,7,18]
    n=len(left)
    print(max_appearing_element(left,right,n))
    print(max_appearing_element_efficient(left,right,n))