# efficient solution

nums = [1, 2, 3, 1]

for number in nums:
    if nums.count(number) != 1:
        return false

return true
