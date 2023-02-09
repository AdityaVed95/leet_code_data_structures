nums = [1, 2, 3, 1]
nums.sort()

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            return True
        else:
            break

return False
