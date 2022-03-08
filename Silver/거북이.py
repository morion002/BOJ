def solution():
  t = int(input())
  dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

  for i in range(t):
    move = list(input())
    posx, posy = 0, 0
    dir = 0
    trace = [(posx, posy)]
    for j in move:
      if j == "F":
        posx += dx[dir]
        posy += dy[dir]
      if j == "B":
        posx -= dx[dir]
        posy -= dy[dir]
      if j == "R":
        if dir == 3:
          dir = 0
        else:
          dir += 1
      if j == "L":
        if dir == 0:
          dir = 3
        else:
          dir -= 1
      trace.append((posx, posy))
    wid = max(trace, key = lambda x : x[0])[0] - min(trace, key = lambda x : x[0])[0]
    len = max(trace, key = lambda x : x[1])[1] - min(trace, key = lambda x : x[1])[1]
    print(wid * len)

if __name__ == "__main__":
  solution()
