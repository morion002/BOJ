def solution():
    n = int(input())
    string = input()
    search = "pPAp"
    
    cnt = 0
    pos = 0
    while True:
        pos = string.find(search, pos)
        if pos == -1:
            break
        cnt += 1
        pos += 4
    
    print(cnt)
    
if __name__ == "__main__":
    solution()
