## Definition:

    Basically arrays are used to store similar type of data together instead of using different variables for storing different types of data. suppose if we consider a scenario where i want to store my facebook friends then i can store them in a single array 

### Operations

Insert - O(n) time complexity  
Search - O(n) for unsorted  
    - O(log n) for sorted (Binary search)  
Delete - At Start/Middle - O(n)  
       - At End - O(1)  
Update - Modify an element - O(1)

### Advantages
-Random Access: Here elements are stored in continuous locations right so we can able access the ith element in constant time.
-Cache Friendliness: cache is a memory which is closest to cpu and ideally you want every item of your program is accessed to be there in cache. That happens in array generally while accessing items the preprocessors will prefetch the items which are at nearby locations.