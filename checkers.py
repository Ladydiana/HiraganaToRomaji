# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22

@author: Culincu Diana Cristina
"""

import dictionary

def isValidHiraganaCharacter(char):
    if char in dictionary.hiragana_list:
        return True
    else:
        return False    


def isValidHiraganaWord(word):
    for i in range(0, len(word)):
        if isValidHiraganaCharacter(word[i])==False:
            return False
    return True

