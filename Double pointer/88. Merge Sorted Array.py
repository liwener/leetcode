"""
双指针 / 从后往前:
用的是倒序的方式。指针i，j，k分别指向num1数组m-1位置，num2数组n-1位置和num1数组m+n-1位置，将i,j指向数值大的放在k位置。

"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l1, l2, l = m-1, n-1, m+n-1

        while l1 >= 0 and l2 >= 0:
            if nums1[l1] < nums2[l2]:
                nums1[l]= nums2[l2]
                l2 -= 1
            else:
                nums1[l] = nums1[l1]
                l1 -= 1

            l -= 1

        # 将nums2数组可能剩下的元素拷贝到nums1数组中
        nums1[:l2+1] = nums2[:l2+1]




