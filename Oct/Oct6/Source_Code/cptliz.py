
import os

def solve(s):
    words = s.split(' ')
    capitalized_words = [w[0].upper() + w[1:] if w else '' for w in words]
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()
