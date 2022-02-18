def solution():
  info = []
  stick = ['E', 'A', 'B', 'C', 'D']
  for i in range(3):
    info.append(list(map(int, input().split())))
  for elem in info:
    print(stick[elem.count(0)])


if __name__ == "__main__":
  solution()
