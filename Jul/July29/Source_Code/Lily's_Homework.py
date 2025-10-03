import os


def lilysHomework(arr):
    ascending = sorted(arr)
    descending = ascending[::-1]

    def count_swaps(target):
        index_map = {value: idx for idx, value in enumerate(target)}
        arr_copy = arr[:]
        visited = [False] * len(arr_copy)
        swap_count = 0

        for i in range(len(arr_copy)):
            if visited[i] or arr_copy[i] == target[i]:
                continue
            cycle_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = index_map[arr_copy[j]]
                cycle_size += 1
            if cycle_size > 0:
                swap_count += (cycle_size - 1)
        return swap_count

    swaps_asc = count_swaps(ascending)
    swaps_desc = count_swaps(descending)

    return min(swaps_asc, swaps_desc)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)
    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
