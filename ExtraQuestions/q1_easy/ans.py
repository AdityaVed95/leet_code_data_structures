# class Solution(object):
#     def shuffle(self, nums, n):
#         """
#         :type nums: List[int]
#         :type n: int
#         :rtype: List[int]
#         """

nums = [2, 5, 1, 3, 4, 7]

n = int(len(nums) / 2)
x = []
y = []

for i in range(0, n):
    x.append(nums[i])

for i in range(n, len(nums)):
    y.append(nums[i])

final = []

for i in range(len(x)):
    final.append(x[i])
    final.append(y[i])

print(final)
