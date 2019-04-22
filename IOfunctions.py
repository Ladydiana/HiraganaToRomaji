# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22

@author: Culincu Diana Cristina
"""

import checkers
import dictionary

def readHiraganaFromKeyboard() :
    word = input('Choose a word: ')
    if (checkers.isValidHiraganaWord(word.strip())==False):
        print('Invalid hiragana word.')
        exit
    #print(word)
    else: 
        return word
    

def romajiCharTranslation(char):
    if(char in dictionary.hiragana_dakuon):
        return dictionary.hiragana_dakuon[char]
    elif(char in dictionary.hiragana_gojuon):
        return dictionary.hiragana_gojuon[char]
    elif(char in dictionary.hiragana_handakuon):
        return dictionary.hiragana_handakuon[char]
    elif(char in dictionary.hiragana_yoon):
        return dictionary.hiragana_yoon[char]
    else:
        print('[Internal Error] Character not found.')
        exit
    


def convertToRomaji(word):
    translation = ''
    for i in range(0, len(word)):
        translation = translation + romajiCharTranslation(word[i])
    return translation



#readHiraganaFromKeyboard()
    