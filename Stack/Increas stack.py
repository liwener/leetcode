class Solution:
    def MaxStack(self, nums):

        size = len(nums)
        l = [0] * size
        r = [0] * size

        stack = []

        for i in range(size):
            # left
            while stack and nums[stack[-1]] > nums[i]:
                r[stack.pop()] = i
            # right
            l[i] = stack[-1] if stack else -1

            stack.append(i)

        while stack:
            r[stack.pop()] = size

        return l, r
