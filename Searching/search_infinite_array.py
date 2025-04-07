def infinite_array_search(arr,key):
    i=0
    while(True):
        if(arr[i]==key):
            return i
        elif(arr[i]>key):
            return -1
        i+=1

if __name__ == "__main__":
    print(infinite_array_search([1,10,200],15))

    