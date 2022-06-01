#!/bin/env python3

import sys,os
from time import sleep
import json
import string
from random import randint,shuffle

# Clearing the Screen
os.system('clear')

files = []
questionsets = []
fgreen = '\033[1;32;40m'
fred = '\033[1;31:40m'
colorreset = '\x1b[0m'

# Read the json db file
sysargvlen = len(sys.argv)
if sysargvlen > 1  :
    for i in range(1, sysargvlen):
        try :
            file=open(sys.argv[i])
            questionsets.extend(json.load(file))
        except :
            print("Cannot open file")
            quit()
else:
    print("Specify the Question Database (json file)")
    quit()
#file=open('questions-v2.json', 'r')
#questionsets=json.load(file)
questions_len=len(questionsets)
questions_asked=[]
scoreBoard = {'correct' : 0, 'wrong' : 0}

questionset_next=randint(0, questions_len-1)

while (questionset_next not in questions_asked) :

    # Question separator
    print("----------------------------------------------------------")

    questions_asked.append(questionset_next)

    print("Question " + str(len(questions_asked)) + " out of " + str(questions_len) + "\n\n")

    questionset_select = questionsets[questionset_next]

    #print question
    print(questionset_select['question'] + "\n")
    
    questionset_select_len = len(questionset_select['options'])
    letterlist = list(string.ascii_uppercase[0:questionset_select_len])

    questionlist = [(k, v) for k, v in questionset_select['options'].items()]
    shuffle(questionlist)

    questionlist_complete = list()

    for i in range(0, len(letterlist)) :
        questionlist_complete.append([letterlist[i], questionlist[i][0], questionlist[i][1]])
    
    # print answer options
    for i in range(0, len(questionlist_complete)) :
        print(str(questionlist_complete[i][0])+". " + str(questionlist_complete[i][1]))
        if questionlist_complete[i][2] == "true" :
            answer = str(questionlist_complete[i][0])
   
    #User Input
    while True :
        response = input("\nSelect the right answer: ").upper()
        if (response == "q") or (response == "Q") :
            quit()
        elif response in letterlist :
            break
        else :
            print(response + " is not an answer option. Answer can be ", end='')
            print(*letterlist, sep=", ")
          
    if (response == answer):
        print(fgreen + "Correct." + colorreset)
        scoreBoard['correct'] = scoreBoard.get('correct', 0) + 1
    else : 
        print("\n" + fred + "Wrong. " + colorreset + "Correct Anser is " + fgreen + answer + colorreset)
        scoreBoard['wrong'] = scoreBoard.get('wrong', 0) + 1
    

    # generate random number as next question
    while (questionset_next in questions_asked) and len(questions_asked) != questions_len  :
        questionset_next=randint(0, questions_len-1)
       
      
    print("\nScore:" + str(scoreBoard['correct']) + " correct, " +  str(scoreBoard['wrong']) + " wrong. \n")

    

    # sleep(2)
    #os.system('clear')
else :
    print("All questions asked.")
    print("Score:" + str(scoreBoard['correct']) + " correct, " +  str(scoreBoard['wrong']) + " wrong.")