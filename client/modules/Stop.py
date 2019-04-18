# -*- coding: utf-8-*-
import random
import re
from client import jasperpath
import sys
import vibrate

WORDS = ["STOP"]


def handle(text, mic, profile):
    
    vibrate.retrieve_from_DOA('high')
    print("Stop module")
    mic.say('Stop')
    
    
        
def isValid(text):
    """
        Returns True if the input is related to jokes/humor.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'STOP', text, re.IGNORECASE))

    




