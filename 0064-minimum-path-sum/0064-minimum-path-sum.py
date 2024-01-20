class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 오른쪽 위에서 왼쪽 아래로 가는 방법 중 최소값
        
        grid_height = len(grid)
        grid_width = len(grid[0])
        
        print('grid_height: ', grid_height)
        print('grid_width: ', grid_width)
        
        for x in range(1, grid_width):
            print('grid[0][x]: ', grid[0][x])
            print('grid[0][x-1]: ', grid[0][x-1])
            grid[0][x] += grid[0][x-1]
            print('after:', grid[0][x])
        
        for y in range(1, grid_height):
            grid[y][0] += grid[y-1][0]
            
        for y in range(1, grid_height):
            for x in range(1, grid_width):
                grid[y][x] += min(grid[y][x-1], grid[y-1][x])
        
        return grid[-1][-1]
            