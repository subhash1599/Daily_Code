def equilibrium_point(arr):
    for i in range(len(arr)):
        ls,rs=0,0
        for j in range(i):
            ls+=arr[j]
        for j in range(i+1,len(arr)):
            rs+=arr[j]
        if ls==rs:
            return True
    return False


if __name__ == "__main__":
    
    print(equilibrium_point([3,4,8,-9,9,7]))
    print(equilibrium_point([3,4,8,-9,20,6]))
    print(equilibrium_point([4,2,-2]))
    print(equilibrium_point([4,2,2]))