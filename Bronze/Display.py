def solution(n, text):
    string = list(text.split())
    cnt = 1
    temp =  ''
    for elem in string:
        if len(temp) + len(elem) > n:
            cnt += 1
            temp = ''
        temp += (elem + " ")
    return cnt

if __name__ == "__main__":
    print(solution(6, "I am Sam"))
    print(solution(20, "A mobile phone is an electronic device used for longrange mobile telecommunications over a cellular network of specialized base stations known as cell sites"))
    print(solution(16, "For each test case output an integer indicating the number of lines needed to display the text according to the manner described above"))
    print(solution(16, "A thumb that completely fills the trough indicates that the entire document is being viewed at which point the scrollbar may temporarily become hidden"))
    print(solution(7, "Abcdefg hijklmn opqrstu vwxyz"))
