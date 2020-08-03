class Solution(object):
    def FloodFill(self, image, sr, sc, newColor):
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1: dfs(r-1, c)
                if r+1 < R: dfs(r+1, c)
                if c >= 1: dfs(r, c-1)
                if c+1 < C: dfs(r, c+1)

        dfs(sr, sc)
        return image

if __name__ == "__main__":
    test = Solution()
    input = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1; sc = 1; newColor = 2

    check = test.FloodFill(input, sr, sc, newColor)
    print(check)