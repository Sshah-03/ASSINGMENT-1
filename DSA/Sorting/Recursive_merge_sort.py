def merge_sort(a):
    n=len(a)
    temp = [None]*n
    sort(a,temp,0,n-1)
             
def sort(a,temp,low,up):
    if low == up:
        return

    mid = (low + up)//2

    sort(a, temp, low, mid) 
    sort(a, temp, mid+1, up) 

    merge(a, temp, low, mid, mid+1, up)

    copy(a, temp, low, up)
    
def merge(a, temp, low1, up1, low2, up2):
    i = low1 
    j = low2 
    k = low1 

    while i <= up1  and j <= up2:
            if a[i] <= a[j]:
                temp[k] = a[i]
                i+=1
            else:
                temp[k] = a[j]
                j+=1
            k+=1
    
    while i <= up1:
                temp[k] = a[i]
                i+=1
                k+=1
            
    while j <= up2:
                temp[k] = a[j]
                j+=1
                k+=1

def copy(a, temp, low, up):
    for i in range(low,up+1):
        a[i] = temp[i]  
             
list1 = [6,3,1,5,9,8]
merge_sort(list1)
print(list1)

list2 = [2,3,5,39,11,8,9,166,45,23]
merge_sort(list2)
print(list2)

list3 = [1,2,3,4,5,6,7,8,9,10]
merge_sort(list3)
print(list3)

list4 = [10,9,8,7,6,5,4,3,2,1]
merge_sort(list4)
print(list4)

list5 = [4]
merge_sort(list5)
print(list5)