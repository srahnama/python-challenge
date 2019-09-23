#search for string like:
#small letter + (GHGlFDS) + small letter
#and save small letter in middle of expression 

def solution():
    text = ''
    # source file is on page source
    with open('src.txt', 'r') as a :
        for l in a.readlines():
            text += l.rstrip()

    i = 0 #counter for capitals
    answer = ''
    c = False #True if there small letter after 3 capital letter
    small_letter=''
    for x in text:
        if i == 6 and c and x.islower(): #if find one
            answer += small_letter
            c = False
            i = 0
        elif x.isupper():# counter for capitals
            i+=1
        elif i == 3 and x.islower() and not c:#check is small letter after 3 cpaitals
            small_letter = x
            c = True
        elif i >= 3 and x.islower() and c:#check that after find small letter exactly 3 capital letter there not more
            c = False
            i = 0
        else:
            c = False
            i = 0
    print(answer)


if __name__ == "__main__":
    solution()

#answer : linkedlist