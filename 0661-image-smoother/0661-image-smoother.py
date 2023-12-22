class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        result = [[0]*n for _ in range(m)]
        
        for x in range(0,m):
            for y in range(0,n):
                sum, count = 0, 0
                for fx in range(-1,2):
                    for fy in range(-1,2):
                        rx = x + fx
                        ry = y + fy
                        if (0 <= rx < m) and (0 <= ry < n):
                            sum += img[rx][ry]
                            count += 1
                result[x][y] = sum//count
                        
        return result
