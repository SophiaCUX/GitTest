#!/usr/bin/env python3
# -*-: coding utf-8 -*-

from hermes_python.hermes import Hermes
import json


MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))



INTENT_LOUD = "Loud"

SessionsStates = {}

def user_loud(hermes, intent_message):
    print("User is asking for noise")

    session_id = intent_message.session_id

    hermes.publish_end_session(session_id, None)


with Hermes(MQTT_ADDR) as h:

    h.subscribe_intent(INTENT_LOUD, user_loud) \
        .start()
