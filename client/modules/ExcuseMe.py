# -*- coding: utf-8-*-
import random
import re
from client import jasperpath
import sys
import vibrate

WORDS = ["EXCUSE", "ME"]


def handle(text, mic, profile):
    
    vibrate.retrieve_from_DOA('low')
    print("ExcuseMe module")
    mic.say('Excuse Me')
    
    
        
def isValid(text):
    """
        Returns True if the input is related to jokes/humor.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'EXCUSE|ME ', text, re.IGNORECASE))

    

