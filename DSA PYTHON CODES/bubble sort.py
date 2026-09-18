arr=[1,7,34,21,65,8]
n=len(arr)

for i in range(n):
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp

print(arr)
