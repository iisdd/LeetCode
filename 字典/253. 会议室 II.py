'''
给你一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间
intervals[i] = [starti, endi] ，为避免会议冲突，同时要考虑充分利用会议室资源，
请你计算至少需要多少间会议室，才能满足这些会议安排。

 

示例 1：

输入：intervals = [[0,30],[5,10],[15,20]]
输出：2
示例 2：

输入：intervals = [[7,10],[2,4]]
输出：1
 

提示：

1 <= intervals.length <= 104
0 <= starti < endi <= 106
'''
# 用时20.8%
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # 天才写法,我服了...求同一时间最多开几场会
        # 把所有start和end时间放一起排序,用1表示start,-1表示end
        time_point = [(i[0], 1)for i in intervals] + [(i[1], -1)for i in intervals]
        time_point.sort(key=lambda x:(x[0], x[1]))      # 如果时间点一样就先减后加
        print(time_point)
        cur = 0
        res = 0
        for i in time_point:
            cur += i[1]
            res = max(res, cur)
        return res
        
        
# 用时87.2%,字典比列表快是常识...
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # 用字典记录起始时间&结束时间,开始+1,结束-1
        dct = {}
        for start, end in intervals:
            dct[start] = dct.get(start, 0) + 1
            dct[end] = dct.get(end, 0) - 1
        time_points = list(dct.items())
        time_points.sort(key=lambda x:x[0])
        cur = 0
        res = 0
        for i in time_points:
            cur += i[1]
            res = max(res, cur)
        return res













        
