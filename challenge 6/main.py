import pickle
import os,glob
import zipfile
import re


#find second solution
#Collecting the comments.
def solution():
    archive = zipfile.ZipFile('/home/mrrobot/www/python/www.pythonchallenge_com/challenge 6/channel.zip', 'r')
    answer = ''
    text_file_name = '90052'
    ext = '.txt'

    while True:
        text_content_b = archive.read(text_file_name + ext)
        text_content = text_content_b.decode('utf-8')

        comment = archive.getinfo(text_file_name + ext).comment

        text_file_name = ''.join([x for x in text_content if x.isdigit()]) #find digits

        if(text_file_name == ''): break

        answer += comment.decode('utf-8')

    print(answer)
   


#find first solution
#answer -> Collect the comments.
def solution1():
    text_name = '90052'
    while True:
        with open('channel/' + text_name + '.txt','r') as input_file:
            text_content = input_file.readline()
            text_name = ''.join([x for x in text_content if x.isdigit()]) #find digits
            print(text_content)
    

def main():
    solution()


if __name__ == "__main__":
    main()
#answer : hockey

#****************************************************************
#****************************************************************
#**                                                            **
#**   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  **
#**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   **
#**   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    **
#**   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     **
#**   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      **
#**   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      **
#**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      **
#**   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      **
#**                                                            **
#****************************************************************
# **************************************************************
