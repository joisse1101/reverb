# -*- coding: utf-8-*-
import logging
#from notifier import Notifier
from brain import Brain
import CarHorn_Detector as detector


class Conversation(object):

    def __init__(self, persona, mic, profile):
        self._logger = logging.getLogger(__name__)
        self.persona = persona
        self.mic = mic
        self.profile = profile
        self.brain = Brain(mic, profile)
        #self.notifier = Notifier(profile)

    def handleForever(self):
        """
        Delegates user input to the handling function when activated.
        """
        self._logger.info("Starting to handle conversation with keyword '%s'.",
                          self.persona)
        while True:
            # Print notifications until empty
            #notifications = self.notifier.getAllNotifications()
            #for notif in notifications:
            #    self._logger.info("Received notification: '%s'", str(notif))

            #ORIGINAL CODE START

            #self._logger.debug("Started listening for keyword '%s'",
            #                   self.persona)
            #threshold, transcribed = self.mic.passiveListen(self.persona)
            #self._logger.debug("Stopped listening for keyword '%s'",
            #                   self.persona)

            #if not transcribed or not threshold:
            #    self._logger.info("Nothing has been said or transcribed.")
            #    continue
            #self._logger.info("Keyword '%s' has been said!", self.persona)

            #self._logger.debug("Started to listen actively with threshold: %r",
            #                   threshold)
            #input = self.mic.activeListenToAllOptions(threshold)
            #self._logger.debug("Stopped to listen actively with threshold: %r",
            #                   threshold)

            #ORIGINAL CODE END

            threshold = self.mic.fetchThreshold()

            input = self.mic.activeListenToAllOptions(threshold)
            print(input)

            if input:
                self.brain.query(input)
            else:
                print("no words detected")
                self._logger.info("Nothing has been said.")
                #print('input[0]: ' + str(input[0]))
                
                #detector.print_prediction(str(input[0]))
                
                #self.mic.say("Pardon?")
