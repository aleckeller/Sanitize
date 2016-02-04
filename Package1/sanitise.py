'''
Created on Nov 6, 2015

@author: aleckeller
'''
import re
def blackout(email,words):
    x = 0
    sentList = []
    sensoredList = []
    #goes through email
    for i in range(0,len(email)):
        found = False
        #finds sentences
        if email[i] == '.' or email[i] == '?'  or email[i] == '!':
            #creates sentence
            sent = email[x:i + 1]
            x = i + 1
            #adds sentences to list
            sentList.append(sent)
            #if one was found, make found true
            found = True 
    #if no period found, email is entire sentence
    if found == False:
        sent = email[x:i + 1]
        sentList.append(sent)        
    #goes through sentences        
    for i in range(0,len(sentList)):
        isSensored = False
        #gets each sentences
        nSent = sentList[i]
        #makes sentence into list of words
        oSent = re.findall(r"[\w']+",nSent)
        #goes through words
        for i in range(0,len(oSent)):
            #creates word without .!?,
            sentWord = oSent[i].translate(None,',.!?')
            #go through list of bad words
            for x in range(0,len(words)):
                #makes bad word lower case
                lWord = words[x].lower()
                lSentWord = sentWord.lower()
                #if the word is equal to one of the bad words
                if lWord == lSentWord:
                    #create a new sentence with a number of @ as long as the sentence length
                    sensored = ('@' * len(nSent))
                    #adds sensored word to sensored list
                    sensoredList.append(sensored) 
                    isSensored = True
        if (isSensored == False):
            #if the sentence does not contain sensored word, add to new list
            sensoredList.append(nSent)         
    #makes list into string
    sensoredSent = ''.join(sensoredList)        
    return sensoredSent