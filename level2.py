def myfunc(nums):
    for i in range(0, len(nums)-1):
        if nums[i:i+2] == [3,3]:
            return True  
    return False
print(myfunc([1,3,3,1]))
print(myfunc([1,3,1,3]))
