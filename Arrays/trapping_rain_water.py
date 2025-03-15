def trapping_rain_water_naive(arr):
    res=0
    for i in range(1,len(arr)-1):
        lmax=arr[i]
        for j in range(i):
            lmax=max(lmax,arr[j])
        rmax=arr[i]
        for j in range(i+1,len(arr)):
            rmax=max(rmax,arr[j])
        res+=min(lmax,rmax)-arr[i]
    return res
if __name__=="__main__":
    print(trapping_rain_water_naive([2,0,2]))
    print(trapping_rain_water_naive([3,0,1,2,5]))
    print(trapping_rain_water_naive([1,2,3]))
    print(trapping_rain_water_naive([3,2,1]))

#water_trapped=min(left max,right max)-arr[i]