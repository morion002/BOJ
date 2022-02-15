def solution():
    n = int(input())
    a = list(map(int, input().split()))
    b, c = map(int, input().split())

    result = n
    for elem in a:
        elem -= b
        if elem > 0:
            while elem > 0:
                elem -= c
                result += 1
    print(result)
    
if __name__ == "__main__":
    solution()
