# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node):
        memo = {}
        def clone(node):
            if node not in memo:
                c = memo[node] = Node(node.val)
                c.neighbors = map(clone, node.neighbors)
            return memo[node]
        return node and clone(node)

    def allPathSourceTarge(self, graph):
        def dfs(cur, path):
            if cur == len(graph)-1:
                res.append(path)
            else:
                for i in graph[cur]:
                    dfs(i, path + [i])

        res = []
        dfs(0,[0])
        return res

if __name__ == "__main__":
    test = Solution()

    input = [[2,4],[1,3],[2,4],[1,3]]
    #test.cloneGraph(input)

    graph = [[1,2],[3],[3],[]]

    print(test.allPathSourceTarge(graph))