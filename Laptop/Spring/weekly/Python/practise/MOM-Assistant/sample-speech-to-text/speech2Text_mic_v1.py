# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 09:55:58 2018

@author: anuryadav
"""

import speech_recognition as sr
r = sr.Recognizer()

#$r.list_microphone_names()
# takes into cosideration mic as source.
mic = sr.Microphone()

with mic as source:
    # listens to the source ie. mic and when the promt changes.
    # what i said is in now audio variable.
    audio = r.listen(source)
type(audio)

# passing to google to give back the text of my speech.
r.recognize_google(audio)
    