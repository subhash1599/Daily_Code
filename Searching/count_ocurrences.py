def count_occurence(arr,key):
    count=0
    for i in range(len(arr)):
        if(arr[i]==key):
            count+=1
            #display the count
    return count

if __name__ == "__main__":
    arr=[1,10,10,10,20,20,40]
    key=5
    print(count_occurence(arr,key))
    arr=[5,10,10,15,20,20,20]
    key=20
    print(count_occurence(arr,key))