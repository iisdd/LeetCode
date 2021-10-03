'''
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]

限制：

0 <= k <= arr.length <= 10000
0 <= arr[i]<= 10000
'''
# 方法一: BIF最小堆(heapq),88.1%, 复杂度O(nlogk), 遍历n个元素, 每次堆排序需要logk次操作
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        import heapq
        li = [-arr[i] for i in range(k)]
        heapq.heapify(li)
        for i in range(k, len(li)):
            heapq.heappush(li, -arr[i])
            heapq.heappop(li)
        return [-x for x in li]


# 方法二: 类似快排,找出第k小的idx然后把比它小的放左边,55.6%
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        # 类似快排,但子集不需要有序
        # 由于递归返回标准值的左边,所以k正好等于长度要单独列出来
        if k == len(arr): return arr
        def loop(l, r):             # 对区间(l, r)排序
            mid = l                 # 中间基准值坐标
            i, j = l, r
            while i < j:
                while i < j and arr[j] >= arr[mid]: j -= 1
                while i < j and arr[i] <= arr[mid]: i += 1
                # 现在i的位置上是一个大于基准值的数,j的位置上是一个小于基准值的数,或者i == j了,所以直接换就行了
                arr[i], arr[j] = arr[j], arr[i]
            # 左右搞定了,把中间的数归位
            # 因为是先动的j再动的i,所以arr[i]肯定是 <= arr[mid]的,直接换就行
            # 终止while循环分两种情况
            # 1.j直接冲到i的位置,上次i停下来的位置肯定有arr[i]<arr[mid](换过的) or arr[i] == arr[mid](i没动过)
            # 2.j停了i往右到j的位置,j停的位置肯定有arr[j]
            arr[mid], arr[i] = arr[i], arr[mid]
            if i > k:
                return loop(l, i-1)
            elif i < k:
                return loop(i+1, r)
            return arr[:i]
        return loop(0, len(arr)-1)




class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == len(arr): return arr
        def findmid(l, r):
            tmp = arr[l]
            while l < r:
                while l < r and arr[r] >= tmp:
                    r -= 1
                arr[l] = arr[r]
                while l < r and arr[l] <= tmp:
                    l += 1
                arr[r] = arr[l]
            arr[l] = tmp
            return l

        l, r = 0, len(arr)-1
        mid = findmid(l, r)
        while mid != k:
            if mid > k:
                r = mid-1
                mid = findmid(l, r)
            elif mid < k:
                l = mid+1
                mid = findmid(l, r)
        return arr[:k]























