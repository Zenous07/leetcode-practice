def maxAreaOfIsland(grid):
    maxArea=0
    m,n=len(grid),len(grid[0])
    def dfs(i,j):
        if i<0 or j<0 or i>=m or j>=n or grid[i][j] !=1:
            return 0
        else:
            grid[i][j]=0
            return 1 + dfs(i+1,j) + dfs(i,j+1) + dfs(i-1,j) + dfs(i,j-1)
    
    for i in range(m):
        for j in range(n):
            if grid[i][j]==1:
                curr=dfs(i,j)
                maxArea=max(maxArea,curr)
    return maxArea