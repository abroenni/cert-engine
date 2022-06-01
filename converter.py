#!/bin/env python3

# Using readlines()
import json
import sys

if len(sys.argv) > 1  :
    try :
        file1=open(sys.argv[1], 'r')
    except :
        print("Cannot open file")
        quit()
else:
    print("Specify the Question Database (json file)")
    quit()

Lines = file1.readlines()

newquestionline = "QUESTION"
examtopic = "Exam Topic"
explanation = "Explanation"
answerline = "Correct Answer:"

counter = 0

datalist = [] 
questionsset = {}
options = {}
block = []

for line in Lines :
    checkline = line
    
    if newquestionline in checkline :
        continue
    if examtopic in checkline :
        continue
    if explanation in checkline :
        continue
    if checkline.startswith(('A. ','B. ','C. ','D. ','E. ')) :
        checkline = checkline[3:]
    if checkline.startswith(answerline) :
        checkline = checkline[-2]
    block.append(checkline.strip())
    
    # If this next line is true, the we have read a questionblock
    if line.startswith(answerline) :
        
        questionsset["question"] = block[0]

        answer=block[-1]
        if answer == 'A':
            anserindex = 1
        if answer == 'B':
            anserindex = 2
        if answer == 'C':
            anserindex = 3
        if answer == 'D':
            anserindex = 4
        if answer == 'E':
            anserindex = 5

        for i in range(1,len(block)-1) :
            if anserindex == i :
                options[block[i]] = "true"
            else :
                options[block[i]] = ""
        
        optionscopy = options.copy()
        questionsset["options"] = optionscopy
        
        # We have to make a copy of the dict, otherwise datalist gests
        # deleted by reference.
        finalquestionset = questionsset.copy()
        datalist.append(finalquestionset)

        block.clear()
        options.clear()
        questionsset.clear()

print(json.dumps(datalist, separators = (", ", " : ")))
