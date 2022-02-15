def solution():
    time = int(input())

    a = time // 300
    time = time % 300
    b = time // 60
    time = time % 60
    c = time // 10
    time = time % 10

    if time == 0:
        print(a, b, c)
    else:
        print(-1)



if __name__ == "__main__":
    solution()
