# -*- coding: utf-8-*-
import os
import re
from getpass import getpass
import yaml
from pytz import timezone
import feedparser
import jasperpath


def run():
    profile = {}

    print("Welcome to the profile populator. If, at any step, you'd prefer " +
          "not to enter the requested information, just hit 'Enter' with a " +
          "blank field to continue.")

    def simple_request(var, cleanVar, cleanInput=None):
        input = raw_input(cleanVar + ": ")
        if input:
            if cleanInput:
                input = cleanInput(input)
            profile[var] = input

    # name
    simple_request('first_name', 'First name')

    #stt settings
    stt_engines = {
        "sphinx": None,
        "google": "GOOGLE_SPEECH"
    }

    response = raw_input("\nIf you would like to choose a specific STT " +
                         "engine, please specify which.\nAvailable " +
                         "implementations: %s. (Press Enter to default " +
                         "to PocketSphinx): " % stt_engines.keys())
    if (response in stt_engines):
        profile["stt_engine"] = response
        api_key_name = stt_engines[response]
        if api_key_name:
            #key = raw_input("\nPlease enter your API key: ")
            profile["keys"] = {api_key_name: "AIzaSyAeTQmFgSKSpZ7TSvnhmhC-eCPVZNY-4es"}
    else:
        print("Unrecognized STT engine. Available implementations: %s"
              % stt_engines.keys())
        profile["stt_engine"] = "sphinx"

    if response == "google":
        response = raw_input("\nChoosing Google means every sound " +
                             "makes a request online. " +
                             "\nWould you like to process the wake up word " +
                             "locally with PocketSphinx? (Y) or (N)?")
        while not response or (response != 'Y' and response != 'N'):
            response = raw_input("Please choose PocketSphinx (Y) " +
                                 "or keep just Google (N): ")
        if response == 'Y':
            profile['stt_passive_engine'] = "sphinx"

    # write to profile
    print("Writing to profile...")
    if not os.path.exists(jasperpath.CONFIG_PATH):
        os.makedirs(jasperpath.CONFIG_PATH)
    outputFile = open(jasperpath.config("profile.yml"), "w")
    yaml.dump(profile, outputFile, default_flow_style=False)
    print("Done.")

if __name__ == "__main__":
    run()
