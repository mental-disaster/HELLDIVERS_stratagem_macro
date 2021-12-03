import keyboard
import pyautogui
from pynput.keyboard import Listener, Key, KeyCode

def handlePress( key ):
    #print( 'Press: {}'.format( key ) )


    if key == Key.esc:
        return False
    #F
    elif key == KeyCode(70):
        pyautogui.keyDown('ctrlleft')
        pyautogui.press('w')
        pyautogui.press('s')
        pyautogui.press('d')
        pyautogui.press('a')
        pyautogui.press('w')
        pyautogui.keyUp('ctrlleft')
    #Railcannon Strike
    #V
    elif key == KeyCode(86):
        pyautogui.keyDown('ctrlleft')
        pyautogui.press('d')
        pyautogui.press('s')
        pyautogui.press('w')
        pyautogui.press('s')
        pyautogui.press('a')
        pyautogui.keyUp('ctrlleft')
    #Heavy Airstrike
    #C
    elif key == KeyCode(67):
        pyautogui.keyDown('ctrlleft')
        pyautogui.press('d')
        pyautogui.press('w')
        pyautogui.press('s')
        pyautogui.press('d')
        pyautogui.press('a')
        pyautogui.keyUp('ctrlleft')
    #Shredder Missile Strike
    #X
    elif key == KeyCode(88):
        pyautogui.keyDown('ctrlleft')
        pyautogui.press('d')
        pyautogui.press('a')
        pyautogui.press('d')
        pyautogui.press('a')
        pyautogui.press('s')
        pyautogui.press('s')
        pyautogui.press('d')
        pyautogui.keyUp('ctrlleft')
    #Thunderer Barrage
    #Z
    elif key == KeyCode(90):
        pyautogui.keyDown('ctrlleft')
        pyautogui.press('d')
        pyautogui.press('s')
        pyautogui.press('w')
        pyautogui.press('w')
        pyautogui.press('a')
        pyautogui.press('s')
        pyautogui.keyUp('ctrlleft')

    #Resupply
    elif key == Key.f1:
        pyautogui.keyDown('ctrlleft')
        pyautogui.press('s')
        pyautogui.press('s')
        pyautogui.press('w')
        pyautogui.press('d')
        pyautogui.keyUp('ctrlleft')
    #Runbler
    elif key == Key.f2:
        pyautogui.keyDown('ctrlleft')
        pyautogui.press('s')
        pyautogui.press('a')
        pyautogui.press('w')
        pyautogui.press('a')
        pyautogui.press('a')
        pyautogui.keyUp('ctrlleft')
    #Jump Pack
    elif key == Key.f3:
        pyautogui.keyDown('ctrlleft')
        pyautogui.press('s')
        pyautogui.press('w')
        pyautogui.press('w')
        pyautogui.press('s')
        pyautogui.press('w')
        pyautogui.keyUp('ctrlleft')
    #drone
    elif key == Key.f4:
        pyautogui.keyDown('ctrlleft')
        pyautogui.press('a')
        pyautogui.press('w')
        pyautogui.press('d')
        pyautogui.keyUp('ctrlleft')
    #Meltal Detector
    elif key == Key.f5:
        pyautogui.keyDown('ctrlleft')
        pyautogui.press('s')
        pyautogui.press('s')
        pyautogui.press('d')
        pyautogui.press('w')
        pyautogui.keyUp('ctrlleft')
            
        
    
def handleRelease(key):
    #print( 'Released: {}'.format( key ) )

    if key == Key.esc:
        return False

with Listener(on_press=handlePress, on_release=handleRelease) as listener:
    listener.join()

'''
while 1:
    #Reinforce
    if keyboard.read_key() == 'f':
        if ~was_pressed:
            was_pressed = True
            pyautogui.keyDown('ctrlleft')
            pyautogui.press('w')
            pyautogui.press('s')
            pyautogui.press('d')
            pyautogui.press('a')
            pyautogui.press('w')
            pyautogui.keyUp('ctrlleft')
    #Railcannon Strike
    elif keyboard.read_key() == 'v':
        if ~was_pressed:
            was_pressed = True
            pyautogui.keyDown('ctrlleft')
            pyautogui.press('d')
            pyautogui.press('s')
            pyautogui.press('w')
            pyautogui.press('s')
            pyautogui.press('a')
            pyautogui.keyUp('ctrlleft')
    #Heavy Airstrike
    elif keyboard.read_key() == 'c':
        if ~was_pressed:
            was_pressed = True
            pyautogui.keyDown('ctrlleft')
            pyautogui.press('d')
            pyautogui.press('w')
            pyautogui.press('s')
            pyautogui.press('d')
            pyautogui.press('a')
            pyautogui.keyUp('ctrlleft')
    #Shredder Missile Strike
    elif keyboard.read_key() == 'x':
        if ~was_pressed:
            was_pressed = True
            pyautogui.keyDown('ctrlleft')
            pyautogui.press('d')
            pyautogui.press('a')
            pyautogui.press('d')
            pyautogui.press('a')
            pyautogui.press('s')
            pyautogui.press('s')
            pyautogui.press('d')
            pyautogui.keyUp('ctrlleft')
    #Thunderer Barrage
    elif keyboard.read_key() == 'z':
        if ~was_pressed:
            was_pressed = True
            pyautogui.keyDown('ctrlleft')
            pyautogui.press('d')
            pyautogui.press('s')
            pyautogui.press('w')
            pyautogui.press('w')
            pyautogui.press('a')
            pyautogui.press('s')
            pyautogui.keyUp('ctrlleft')

    #Resupply
    elif keyboard.read_key() == 'f1':
        if ~was_pressed:
            was_pressed = True
            pyautogui.keyDown('ctrlleft')
            pyautogui.press('s')
            pyautogui.press('s')
            pyautogui.press('w')
            pyautogui.press('d')
            pyautogui.keyUp('ctrlleft')
    #Runbler
    elif keyboard.read_key() == 'f2':
        if ~was_pressed:
            was_pressed = True
            pyautogui.keyDown('ctrlleft')
            pyautogui.press('s')
            pyautogui.press('a')
            pyautogui.press('w')
            pyautogui.press('a')
            pyautogui.press('a')
            pyautogui.keyUp('ctrlleft')
    #Jump Pack
    elif keyboard.read_key() == 'f3':
        if ~was_pressed:
            was_pressed = True
            pyautogui.keyDown('ctrlleft')
            pyautogui.press('s')
            pyautogui.press('w')
            pyautogui.press('w')
            pyautogui.press('s')
            pyautogui.press('w')
            pyautogui.keyUp('ctrlleft')
    #drone
    elif keyboard.read_key() == 'f4':
        if ~was_pressed:
            was_pressed = True
            pyautogui.keyDown('ctrlleft')
            pyautogui.press('a')
            pyautogui.press('w')
            pyautogui.press('d')
            pyautogui.keyUp('ctrlleft')
    #Meltal Detector
    elif keyboard.read_key() == 'f5':
        if ~was_pressed:
            was_pressed = True
            pyautogui.keyDown('ctrlleft')
            pyautogui.press('s')
            pyautogui.press('s')
            pyautogui.press('d')
            pyautogui.press('w')
            pyautogui.keyUp('ctrlleft')
            
    elif keyboard.read_key() == 'esc':
            break
    else:
        was_pressed = False
'''
