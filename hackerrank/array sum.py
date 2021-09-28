import os
def compareTriplets(a, b):
    # Write your code here
    ap=0
    bp=0
    n = int(input())
    for i in range(n):
        if a[i]>b[i]:
            ap+=1
        elif b[i]>a[i]:
            bp+=1
        else:
            continue
    return ap,bp
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()