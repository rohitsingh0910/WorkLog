
def numSubmat(self, mat):
        if not mat:
            return 0

        m, n = len(mat), len(mat[0])
        heights = [0] * n
        result = 0

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0

            result += self.count_rectangles(heights)

        return result

def count_rectangles(self, heights):
        stack = []
        total = 0
        for i in range(len(heights) + 1):
            while stack and (i == len(heights) or heights[stack[-1]] > heights[i]):
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                total += h * w
            stack.append(i)

        return total

print(numSubmat([[1,0,1],[1,1,0],[1,1,0]]))