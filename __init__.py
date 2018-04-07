
from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

import random

class GoRandomSkill(MycroftSkill):


    def __init__(self):
        super(GoRandomSkill, self).__init__(name="GoRandomSkill")

    def initialize(self):
        self.load_data_files(dirname(__file__))

        coin_flip_intent = IntentBuilder("CoinFlipIntent").require("CoinFlipKeyword").build()
        self.register_intent(coin_flip_intent, self.handle_coin_flip_intent)

    def handle_coin_flip_intent(self, message):
        self.speak_dialog("flip.coin")
        if bool(random.getrandbits(1)):
            self.speak_dialog("heads")
        else:
            self.speak_dialog("tails")

    def stop(self):
        pass

def create_skill():
    return CoinFlipSkill()
