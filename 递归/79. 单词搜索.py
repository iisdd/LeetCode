'''
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，
其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
同一个单元格内的字母不允许被重复使用。

示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false
 
提示：

board 和 word 中只包含大写和小写英文字母。
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
'''
# 用时92.8%,目前做过的最难的题了...
class Solution:
    directions = [(0,-1), (-1,0), (0,1), (1,0)]         # 搜索顺序:左上右下
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        # 二维列表marked记录是否走过这个点
        marked = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # 以每一个格子为起点搜索,0代表word的第一个字母
                if self.is_head(board, word, 0, i, j, marked, m, n):
                    return True
        return False
    # 需要构建辅助函数is_head,关键技术!!!
    def is_head(self, board, word, index,
                start_x, start_y, marked, m, n):        # 递归实现搜索
        # 先声明终止条件
        if index == len(word) - 1:
            return board[start_x][start_y] == word[index]
        # 这一步相同,继续探索下一步
        if board[start_x][start_y] == word[index]:
            # 先占住这个位置,搜索不成功再释放
            marked[start_x][start_y] = True
            for direction in self.directions:
                new_x = start_x + direction[0]
                new_y = start_y + direction[1]
                # 如果找寻成功(界内,下个点没走过,下个点is_head),返回True
                if 0<=new_x<m and 0<=new_y<n and \
                   not marked[new_x][new_y] and \
                   self.is_head(board, word, index+1,
                                new_x, new_y,
                                marked, m, n):
                    return True
            # 这个点不能当head,释放这个点
            marked[start_x][start_y] = False
        return False
    
                    
        























        
