"""
由于遍历一个图有两种方式：bfs和dfs。所以深拷贝一个图也可以采用这两种方法。
"""

# BFS (广度遍历)
"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return None
        visted = {}
        clone = Node(node.val, [])  # 拷贝，生成新结点
        visted[node] = clone

        queue = [node]  # 旧结点
        while (queue):  # 遍历图
            now = queue.pop(0)
            for tmp in now.neighbors:
                if tmp not in visted:
                    visted[tmp] = Node(tmp.val, [])  # 拷贝，生成新结点
                    # 访问标记并生成新结点
                    queue.append(tmp)
                visted[now].neighbors.append(visted[tmp])  # 复制邻居结点

        return clone



