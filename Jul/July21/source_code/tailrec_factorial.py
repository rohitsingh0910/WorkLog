def tail_fact(n, acc=1):
    return acc if n <= 1 else tail_fact(n-1, acc*n)

if __name__ == "__main__":
    print(tail_fact(100))
