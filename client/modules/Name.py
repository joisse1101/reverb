# -*- coding: utf-8-*-
import random
import re
from client import jasperpath
import sys
import vibrate

WORDS = ["JOYCE", "TIFFANY", "PROF"]


def handle(text, mic, profile):
    
    vibrate.retrieve_from_DOA('low')
    print("Name module")
    mic.say('Name')
    
    
        
def isValid(text):
    """
        Returns True if the input is related to jokes/humor.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'JOYCE|TIFFANY|PROF', text, re.IGNORECASE))

    


