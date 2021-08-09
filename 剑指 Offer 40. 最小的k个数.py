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
# 方法一: 最小堆(heapq),88.1%, 复杂度O(nlogk), 遍历n个元素, 每次堆排序需要logk次操作
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
        # 特殊边界
        if k == len(arr): return arr
        def loop(s, e):             # s:起点, e:终点
            # 把arr从s开始到e,以标称值为中间点切割成两半(左边值都比中间点小,右边大)
            m = s                   # m为标称值的idx(取第一个数)
            i, j = s, e
            while i < j:            # 先移右边,因为m选的左边的数,如果选的右边的数就是先移左边
                while i < j and arr[j] >= arr[m]:
                    j -= 1
                while i < j and arr[i] <= arr[m]:
                    i += 1
                if i < j:
                    arr[i], arr[j] = arr[j], arr[i]     # 快排,左右互换保持左小右大
            arr[m], arr[i] = arr[i], arr[m]             # 中间值归位
            if i == k:
                return arr[ : i]
            elif i > k:
                return loop(s, i-1)
            else:
                return loop(i+1, e)
        return loop(0, len(arr)-1)







