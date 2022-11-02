def removeDuplicates(nums):
    nums[:] = sorted(set(nums))
    return len(nums)

nums = [1,1,2,2,3,3,4,4,5,5]
print(removeDuplicates(nums))