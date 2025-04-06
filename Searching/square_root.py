def square_root(n):
    i=1
    while(i*i<=n):
        i+=1
    return i-1


def square_root_binary_search(n):
    low=1
    high=n
    while(low<=high):
        mid=(low+high)//2
        if(mid*mid==n):
            return mid
        elif(mid*mid<n):
            low=mid+1
        else:
            high=mid-1
    return high


if __name__ == '__main__':
    print(square_root(9))
    print(square_root_binary_search(10))