for _ in range(t):
    n, target = input().split()
    n = int(n)
    target = int(target)
    arr = [int(x) for x in input().split()]
    result = sum_subarray(arr, target)
    if result[0] == -1:
        print(-1)
    else:
        print(result[0], result[1])
