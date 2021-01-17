'''
在一个 XY 坐标系中有一些点，我们用数组 coordinates 来分别记录它们的坐标，
其中 coordinates[i] = [x, y] 表示横坐标为 x、纵坐标为 y 的点。

请你来判断，这些点是否在该坐标系中属于同一条直线上，是则返回 true，
否则请返回 false。

示例 1：

输入：coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
输出：true
示例 2：

输入：coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
输出：false
 
提示：

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates 中不含重复的点
'''
# 用时21.5%
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        p = coordinates                                 # 变量名太长了,换一个
        if n == 2:
            return True
        # 除法不如乘法,不用考虑除0的情况
        # 遍历y2: (y3-y2)/(x3-x2) == (y2-y1)/(x2-x1)
        # (y3-y2)*(x2-x1) == (y2-y1)*(x3-x2)
        for i in range(1, n-1):
            if (p[i+1][1]-p[i][1])*(p[i][0]-p[i-1][0]) != (p[i][1]-p[i-1][1])*(p[i+1][0]-p[i][0]):
                return False
        return True
        






















        
