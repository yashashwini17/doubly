def qs(arr,low,high):
    if(low>=high):
        return
    pIndex=getPIndex(arr,low,high)
    qs(arr,low,pIndex-1)
    qs(arr,pIndex+1,high)
def getPIndex(arr,low,high):
    pivot=arr[low]
    i=low
    j=high
    while(i<j):
        while(arr[i]<=pivot and i<high):
            i+=1
        while(arr[j]>pivot and j>low):
            j-=1
        if(i<j):
            arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j
arr=list(map(int,input().split()))
low=0
high=len(arr)-1
qs(arr,low,high)
print(arr)
