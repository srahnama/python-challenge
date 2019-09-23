import urllib.request

def solution():
    
    url_digit = "12345" #first digits for request
    for i in range(0, 500):
        pc_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + url_digit #url for request
        data = urllib.request.urlopen(pc_url) 
        url_text = "".join( chr(x) for x in bytearray(data.read()) ) #bytes to string
        url_digit = ''.join([x for x in url_text if x.isdigit()]) #find digits
        print(i , url_text)
        # try:
        #     data1 = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/"+url_digit+".html") 
        # except:
        #     continue
        # if data1.getcode()==200:
        #     print(url_digit)
            

    

if __name__ == "__main__":
    solution()

#answer : peak.html