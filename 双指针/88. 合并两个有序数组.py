'''
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nums2 的元素。

示例 1：

输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
示例 2：

输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]
 
提示：

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[i] <= 109
'''
# 用时57.5%
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 特殊情况
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
        # 鉴于nums1后面全是0,可以从后面往前排
        p1 = m-1                            # nums1指针
        p2 = n-1                            # nums2指针
        i = m+n-1                           # 添加元素的指针
        while i >= 0 and p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1
            i -= 1
        # 收尾,如果p1先到-1就要把p2的补全,如果p2先到-1那p1就不用管了,自然顺序就行
        if i >= 0:
            while i >= 0 and p2 >= 0:
                nums1[i] = nums2[p2]
                p2 -= 1
                i -= 1
    
                
        








        
