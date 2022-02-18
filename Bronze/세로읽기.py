def solution(string):
  max_len = 0
  for elem in string:
    max_len = max(max_len, len(elem))
  
  result = ""
  for i in range(max_len):
    temp = ""
    for elem in string:
      if i < len(elem):
        temp += elem[i]
      else:
        continue
    result += temp
  return result


if __name__ == "__main__":
  print(solution(["AABCDD", "afzz", "09121", "a8EWg6", "P5h3kx"]))
  print(solution(["ABCDE", "abcde", "01234", "FGHIJ", "fghij"]))
