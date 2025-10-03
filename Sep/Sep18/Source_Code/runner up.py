if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max_score = max(arr)
    filtered_scores = [score for score in arr if score != max_score]
    print(max(filtered_scores))
