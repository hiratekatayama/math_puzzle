class Solution(object):
    def allPathSourceTarget(self, graph):
        def dfs(cur, path):
            if cur == len(graph) - 1:
                res.append(path)
            else:
                for i in graph[cur]:
                    dfs(i, path + [i])
        res = []
        dfs(0, [0])
        return res

if __name__ == "__main__":
    test = Solution()
    graph = [[1,2],[3],[3],[]]
    print(len(graph))
    print(test.allPathSourceTarget(graph))