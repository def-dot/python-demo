# https://leetcode.cn/problems/all-paths-from-source-to-target/solution/suo-you-ke-neng-de-lu-jing-by-leetcode-s-iyoh/
# dag有向无环图，找到0到n-1节点的所有路径
# 深度优先遍历 DFS 广度优先遍历 BFS


def dfs_t(graph):
    # 深度优先遍历
    res = list()
    stk = list()

    def dfs(x: int):
        if x == len(graph) - 1:
            res.append(stk[:])
            return

        for y in graph[x]:
            stk.append(y)
            dfs(y)
            stk.pop()

    stk.append(0)
    dfs(0)
    return res


def bfs_t(graph):
    # 广度优先遍历
    res = []
    queue = [[0]]
    while queue:
        item = queue.pop()
        index = item[-1]
        direct = graph[index]
        for ii in direct:
            new_item = item[:]
            new_item.append(ii)
            if ii == len(graph) - 1:
                res.append(new_item)
            else:
                queue.append(new_item)
    return res


if __name__ == '__main__':
    # 0->1,2  1->3 2->3 3->null
    graph = [[1, 2], [3], [3], []]
    # res = dfs_t(graph)
    res = bfs_t(graph)
    print(res)
