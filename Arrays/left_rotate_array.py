def left_rotate_array(arr,rotate):
    return arr[rotate:]+arr[:rotate]


def left_rotate_another(arr):
    temp=arr[0]
    n=len(arr)
    for i in range(1,len(arr)):
        arr[i-1]=arr[i]
    arr[n-1]=temp
    return arr

if __name__=="__main__":
    print(left_rotate_array([1,2,3,4,5],2))
    # print(left_rotate_array([30,5,20]))
    # print(left_rotate_another([30,5,20]))
