"""
将四数之和转化为三数和
三数之和转换为两数和
"""

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        size = len(nums)

        if size < 4:
            return
        res = []
        nums.sort()

        for i in range(siz e -3):
            # 去重
            if  i > 0 and nums[i ]== nums[ i -1]:
                continue

                # 将四数之和转化为三数和
            newtarget = target - nums[i]
            for j in range( i +1, size -2):
                # 去重
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                l, r = j + 1, size - 1

                while l < r:
                    threesum = nums[j] + nums[l] + nums[r]
                    if threesum == newtarget:
                        res.append([nums[i], nums[j], nums[l], nums[r]])

                        l += 1
                        r -= 1
                        # 去重
                        while l < r and nums[l] == nums[l - 1]:
                            l -= 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1

                    elif threesum < newtarget:
                        l += 1
                    else:
                        r -= 1

        return res

