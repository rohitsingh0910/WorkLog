import os
def surfaceArea(A):
    H = len(A)
    W = len(A[0])

    top = H * W
    bottom = H * W
    front = 0
    rear = 0
    left = 0
    right = 0
    for i in range(H):
        for j in range(W):
            if i == 0:
                front += A[i][j]
            else:
                front += max(0, A[i][j] - A[i - 1][j])

            if i == H - 1:
                rear += A[i][j]
            else:
                rear += max(0, A[i][j] - A[i + 1][j])

            if j == 0:
                left += A[i][j]
            else:
                left += max(0, A[i][j] - A[i][j - 1])
            if j == W - 1:
                right += A[i][j]
            else:
                right += max(0, A[i][j] - A[i][j + 1])

    return top + bottom + front + rear + left + right


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)
    print(result)
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
