#Approach - just start traversing from the given start indexes sr, sc. check all foor directions if they are equal to the intial color change their color to given color and traverse
# TC - O(nxm), SC-O(nxm)
def floodFill(image, sr, sc, color):
    n = len(image)
    m = len(image[0])
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    initial_color = image[sr][sc]

    def dfs(r, c, image):
        image[r][c] = color # change the color if visiting

        for rr, cc in directions:
            nr = r+rr
            nc = c+cc

            if nr>=0 and nr<n and nc>=0 and nc<m and image[nr][nc] == initial_color: #compare with the intial color to traverse further and also check the boundaries
                dfs(nr, nc, image)

    dfs(sr, sc, image) #start from give start indexes
    return image

floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)