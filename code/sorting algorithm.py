arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
i=0
j=0
result=[]
# to compare and take small elements
while(i<len(arr1)and j<len(arr2)):
    if(arr1 [i]<=arr2[j]):
        result.append(arr1[i])
        i+=1
    else:
        result.append(arr2[j])
        j+=1
#to take rest of elements in arr1
while(i<len(arr1)):
    result.append(arr1[i])
    i+=1
#to take rest of elements in arr2
while(j<len(arr2)):
    result.append(arr2[j])
    j+=1
print(result)
        