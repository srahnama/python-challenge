import pickle

def solution():
    
    code_of_input = ''
    with open('banner.p','r') as input_file:
       
        for x in input_file.readlines():
            code_of_input += x
        decode_input = pickle.loads(bytes(code_of_input,encoding='ascii'))
        for x in decode_input:
            for i in x:
                print(i[0]*i[1], end='')
            print()
            

    

if __name__ == "__main__":
    solution()

#answer : channel