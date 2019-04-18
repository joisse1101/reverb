# -*- coding: utf-8-*-
import random
import re
from client import jasperpath
import sys
import vibrate

WORDS = ["WATCH", "OUT"]


def handle(text, mic, profile):
    
    vibrate.retrieve_from_DOA('high')
    print("WatchOut module")
    mic.say('Watch Out')
    
    
        
def isValid(text):
    """
        Returns True if the input is related to jokes/humor.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'WATCH|OUT', text, re.IGNORECASE))

    



