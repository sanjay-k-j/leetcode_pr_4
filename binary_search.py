# Binary search in a array
print("Enter the sorted array")
arr = list(map(int,input().split()))
key =int(input("Enter the key : "))
lo = 0
hi = len(arr) -1 

def fun(lo,hi):
    while lo <= hi:
        mid =(lo+hi)//2
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            return fun(lo,mid-1)
        else :
            return fun(mid+1,hi)
    return -1

print(fun(lo,hi) )
