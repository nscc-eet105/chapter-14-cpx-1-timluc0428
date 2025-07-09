from adafruit_circuitplayground import cp
import time
import random

MAX_PIXEL = 9

music_notes = {
    "A4":440, 
    "B4":494, 
    "C5":523, 
    "D5":587, 
    "E5":659, 
    "F5":698, 
    "G5":784, 
    "A5":880, 
    "B5":988, 
    "C6":1047
    }

colors = {
    "BLACK":(0, 0, 0),
    "RED":(255, 0, 0),
    "GREEN":(0, 255, 0),
    "BLUE":(0, 0, 255),
    "YELLOW":(255, 255, 0),
    "PURPLE":(255, 0, 255),
    "CYAN":(0, 255, 255),
    "WHITE":(255, 255, 255),
}

#I turned down the brightness because it was giving me a headache at full brightness
cp.pixels.brightness = .05

def fill_pixels(color):
    for pixel in range(MAX_PIXEL + 1):
        cp.pixels[pixel] = color

while True:
    if cp.touch_A1:
        cp.start_tone(music_notes["C5"])
        fill_pixels(colors["RED"])
    
    elif cp.touch_A6:
        cp.start_tone(music_notes["D5"])
        fill_pixels(colors["WHITE"])
        
    elif cp.touch_A2:
        cp.start_tone(music_notes["E5"])
        fill_pixels(colors["BLUE"])
        
    elif cp.touch_A5:
        cp.start_tone(music_notes["G5"])
        fill_pixels(colors["PURPLE"])
    else:
        cp.stop_tone()
        fill_pixels(colors["BLACK"])