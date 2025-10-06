def minion_game(string):
    vowels = 'AEIOU'
    kevin = 0
    stuart = 0
    n = len(string)

    for i in range(n):
        if string[i] in vowels:
            kevin += n - i
        else:
            stuart += n - i

    if kevin > stuart:
        print(f"Kevin {kevin}")
    elif stuart > kevin:
        print(f"Stuart {stuart}")
    else:
        print("Draw")

    # string=list(string)
    # vowels=['A','E','I','O','U']
    # i=0
    # stuart=0
    # kevin=0
    # while True:
    #     if string[i] in vowels:
    #         stuart+=len(string)
    #     else:
    #         kevin+=len(string)
    #     string.pop(0)
    # if stuart>kevin:
    #     print(f'Stuart {stuart}')
    # else:
    #     print(f"Kevin {kevin}")


if __name__ == '__main__':
    s = input()
    minion_game(s)