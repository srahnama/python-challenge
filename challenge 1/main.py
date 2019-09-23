#ord(K) - ord(M) = -2

def solution():
    first_string="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    url_string = "map"
    answer = ''
    for x in url_string:
        if x == "z":
            answer += 'b' 
        elif x=='y':
            answer += 'a' 
        elif x.isalpha() and x != " " :
            answer += chr(ord(x)+2) 
        else:
            answer += x
    print(answer)


if __name__ == "__main__":
    solution()

#answer : ocr