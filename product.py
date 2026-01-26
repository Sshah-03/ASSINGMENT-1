def productself(nums):
    n = len(nums)
    output = [1] * n
    for i in range(n):
        product = 1
        for j in range(n):
            if 1 != j:
                product *= nums[j]
        output[i] = product
    return output
nums = [1, 2, 3, 4]
print("Product except self: ", productself(nums))
