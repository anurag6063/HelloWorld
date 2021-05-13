# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 09:06:39 2018

@author: anuryadav
"""

import speech_recognititon as sr

r = sr.Recognizer()

harvard = sr.AudioFile("C:/Users/anuryadav/Desktop/Python/practise/MOM-Assistant/sample-speech-to-text/hello-yes.wav")

with harvard as source:
    audio = r.record(source)
    
type(audio)

r.recognize_google(audio)


"""
Waveform Audio File Format (WAVE, or more commonly known as WAV
 due to its filename extension - both pronounced "wave"[6])[3][7][8][9] (rarely, Audio for Windows)
[10] is a Microsoft and IBM audio file format standard for storing an audio bitstream on PCs. 
It is an application of the Resource Interchange File Format (RIFF) bitstream format method 
for storing data in "chunks", and thus is also close to the 8SVX and the AIFF format used on Amiga and Macintosh computers, respectively. It is the main format used on Microsoft Windows systems for raw and typically uncompressed audio. The usual bitstream encoding is the linear pulse-code modulation (LPCM) format.

"""