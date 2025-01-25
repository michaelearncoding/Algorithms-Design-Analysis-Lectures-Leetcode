def bfs(graph, s):
    visited = [False] * len(graph)  # 初始化一个列表，记录每个节点是否被访问过
    q = deque([s])  # 使用双端队列来存储待访问的节点，初始时包含起始节点 s
    visited[s] = True  # 标记起始节点 s 为已访问
    step = 0  # 记录从起始节点 s 到当前节点的步数
    
    while q:  # 当队列不为空时，继续遍历
        sz = len(q)  # 当前队列中的节点数
        for i in range(sz):  # 遍历当前层的所有节点
            cur = q.popleft()  # 从队列中取出一个节点
            print(f"visit {cur} at step {step}")  # 打印当前访问的节点和步数
            if cur == target:  # 判断是否到达目标节点
                return step  # 如果到达目标节点，返回步数

            for to in neighborsOf(cur):  # 遍历当前节点的所有邻居节点
                if not visited[to]:  # 如果邻居节点未被访问
                    q.append(to)  # 将邻居节点加入队列
                    visited[to] = True  # 标记邻居节点为已访问
        step += 1  # 每遍历完一层，步数加一
    
    return -1  # 如果遍历完所有节点仍未找到目标节点，返回 -1