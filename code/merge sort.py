def mergeSort(arr,low,high):
    if(low>=high):
        return
    mid=(low+high)//2
    mergeSort(arr,low,mid)
    mergeSort(arr,mid+1,high)
    sort(arr,low,mid,high)
def sort(arr,low,mid,high):
    i=low
    j=mid+1
    k=[]
    while(i<=mid and j<=high):
        if(arr[i]<=arr[j]):
            k.append(arr[i])
            i+=1
        else:
            k.append(arr[j])
            j+=1
    while(i<=mid):
        k.append(arr[i])
        i+=1
    while(j<=high):
        k.append(arr[j])
        j+=1
    for ind,val in enumerate(k):
        arr[low+ind]=val
arr=list(map(int,input().split()))
low=0
high=len(arr)-1
mergeSort(arr,low,high)
print(arr)










