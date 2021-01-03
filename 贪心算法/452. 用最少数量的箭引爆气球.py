'''
在二维空间中有许多球形的气球。对于每个气球，提供的输入是水平方向上，
气球直径的开始和结束坐标。由于它是水平的，
所以y坐标并不重要，因此只要知道开始和结束的x坐标就足够了。
开始坐标总是小于结束坐标。平面内最多存在104个气球。

一支弓箭可以沿着x轴从不同点完全垂直地射出。
在坐标x处射出一支箭，若有一个气球的直径的开始和结束坐标为 xstart，xend，
且满足  xstart ≤ x ≤ xend，则该气球会被引爆。可以射出的弓箭的数量没有限制。
弓箭一旦被射出之后，可以无限地前进。我们想找到使得所有气球全部被引爆，
所需的弓箭的最小数量。

Example:

输入:
[[10,16], [2,8], [1,6], [7,12]]

输出:
2

解释:
对于该样例，我们可以在x = 6（射爆[2,8],[1,6]两个气球）和 x = 11（射爆另外两个气球）。
'''
# 用时92.3%
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # 排序后遍历,维护tail,贪心算法
        if points == []:
            return 0
        points.sort()
        tail = points[0][1]
        res = 1                         # 只要有气球就从1数起
        for point in points:
            if point[0] > tail:         # 新的区间不重叠
                res += 1
                tail = point[1]
            elif point[1] < tail:       # 新的区间有重叠且尾巴比较小
                tail = point[1]
        return res

    
