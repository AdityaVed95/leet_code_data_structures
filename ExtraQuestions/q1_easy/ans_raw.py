class Solution(object):
    def shuffle(self, nums, n):
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

        return final
