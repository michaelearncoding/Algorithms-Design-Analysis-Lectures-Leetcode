
'''
# Hi Michael,
Thank you for your time today. Happy to move your application forward to the technical interview. 

Are you open tomorrow, May 15th, anytime from 10:30 am - 5 pm ET for this interview? If not, please share 3-4 of your 60-minute availability on the 19th, 21st and 22nd. Ideally, we'd like to have this interview tomorrow. The technical interview will include a coding logic test, a CSP rule construction test, and an AI prompt creation test.

'''




# 多叉树的层序遍历写法是这样：
def bfs(graph, s):
    visited = [False] * len(graph)
    from collections import deque
    q = deque([s])
    visited[s] = True

    while q:
        cur = q.popleft()
        print(f"visit {cur}")
        for e in graph.neighbors(cur):
            if not visited[e.to]:
                q.append(e.to)
                visited[e.to] = True


# 图结构的 BFS 遍历是类似的：

# 图结构的 BFS 遍历，从节点 s 开始进行 BFS
def bfs(graph, s):
    visited = [False] * len(graph)
    from collections import deque
    q = deque([s])
    visited[s] = True

    while q:
        cur = q.popleft()
        print(f"visit {cur}")
        for e in graph.neighbors(cur):
            if not visited[e.to]:
                q.append(e.to)
                visited[e.to] = True


# 第二种能够记录遍历步数的写法。
# 多叉树的层序遍历写法是这样：
from collections import deque

def levelOrderTraverse(root):
    if root is None:
        return
    q = deque()
    q.append(root)
    # 记录当前遍历到的层数（根节点视为第 1 层）
    depth = 1

    while q:
        sz = len(q)
        for i in range(sz):
            cur = q.popleft()
            # 访问 cur 节点，同时知道它所在的层数
            print(f"depth = {depth}, val = {cur.val}")

            for child in cur.children:
                q.append(child)
        depth += 1


# 图结构的 BFS 遍历是类似的：
from collections import deque

# 从 s 开始 BFS 遍历图的所有节点，且记录遍历的步数
def bfs(graph, s):
    visited = [False] * len(graph) 
    q = deque([s])
    visited[s] = True
    # 记录从 s 开始走到当前节点的步数
    step = 0
    
    while q:
        sz = len(q)
        for i in range(sz):
            cur = q.popleft()
            print(f"visit {cur} at step {step}")
            for e in graph.neighbors(cur):
                if not visited[e.to]: 
                    q.append(e.to)
                    visited[e.to] = True
        step += 1



# 
# 写法三
# 第三种能够适配不同权重边的写法。

