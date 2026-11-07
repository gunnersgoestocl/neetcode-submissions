class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        r = len(matrix) // 2
        n = len(matrix) - 1
        for i in range(1, r+1):
            upper = r+i if len(matrix) % 2 == 1 else r+i-1
            lower = r-i
            for j in range(lower, upper):
                a = matrix[lower][j]
                # north to east
                print(j, upper)
                b = matrix[j][upper]
                matrix[j][upper] = a
                a = b
                # east to south
                print(upper, n-j)
                b = matrix[upper][n-j]
                matrix[upper][n-j] = a
                a = b
                # south to west
                print(n-j, lower)
                b = matrix[n-j][lower]
                matrix[n-j][lower] = a
                # west to north
                print(lower, j)
                matrix[lower][j] = b