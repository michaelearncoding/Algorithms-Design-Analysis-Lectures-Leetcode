//这个多叉树的遍历框架就可以延伸出 
// 回溯算法框架套路详解 中的回溯算法框架：
// 回溯算法框架
void backtrack(...) {
    // base case
    if (...) return;

    for (int i = 0; i < ...; i++) {
        // 做选择
        ...

        // 进入下一层决策树
        backtrack(...);

        // 撤销刚才做的选择
        ...
    }
}

// # i.e.

// 回溯算法核心部分代码
void backtrack(int[] nums) {
    // 回溯算法框架
    for (int i = 0; i < nums.length; i++) {
        // 做选择
        used[i] = true;
        track.addLast(nums[i]);

        // 进入下一层回溯树
        backtrack(nums);

        // 取消选择
        track.removeLast();
        used[i] = false;
    }
}


// dfs

// DFS 算法核心逻辑
void dfs(int[][] grid, int i, int j) {
    int m = grid.length, 
    n = grid[0].length;

    if (i < 0 || j < 0 || i >= m || j >= n) {
        return;
    }

    if (grid[i][j] == 0) {
        return;
    }

    // 遍历过的每个格子标记为 0

    grid[i][j] = 0;
    dfs(grid, i + 1, j);
    dfs(grid, i, j + 1);
    dfs(grid, i - 1, j);
    dfs(grid, i, j - 1);
}

