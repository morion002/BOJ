def solution():
  h, m = map(int, input().split())
  if m >= 45:
    m -= 45
  else:
    h -= 1
    if h < 0:
      h = 23
    m = (m + 60) - 45
  print(h, m)

if __name__ == "__main__":
  solution()
