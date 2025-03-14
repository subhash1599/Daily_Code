def stock_buy_and_sell(arr):
    c,temp=0,0
    for i in range(len(arr)-1):
        if arr[i]<arr[i+1]:
            temp=arr[i+1]-arr[i]
            c+=temp
    return c
if __name__=="__main__":
    print(stock_buy_and_sell([1,5,3,8,12]))
    print(stock_buy_and_sell([30,20,10]))
    print(stock_buy_and_sell([10,20,30]))
    print(stock_buy_and_sell([1,5,3,1,2,8]))