import keyboard
import pyautogui
from pynput.keyboard import Listener, Key, KeyCode

def pressKeys(*args):
    for key in args:
        pyautogui.press(key)

def handlePress(key):
    #print( 'Press: {}'.format( key ) )
    if key == Key.esc:
        return False
    #Reinforce
    elif key == KeyCode(char='f'):
        pyautogui.keyDown('ctrlleft')
        pressKeys('w','s','d','a','w')
        pyautogui.keyUp('ctrlleft')
    #Railcannon Strike
    elif key == KeyCode(char='v'):
        pyautogui.keyDown('ctrlleft')
        pressKeys('d','s','w','s','a')
        pyautogui.keyUp('ctrlleft')
    #Heavy Airstrike
    elif key == KeyCode(char='c'):
        pyautogui.keyDown('ctrlleft')
        pressKeys('d','w','s','d','a')
        pyautogui.keyUp('ctrlleft')
    #Shredder Missile Strike
    elif key == KeyCode(char='x'):
        pyautogui.keyDown('ctrlleft')
        pressKeys('d','a','d','a','s','s','d')
        pyautogui.keyUp('ctrlleft')
    #Thunderer Barrage
    elif key == KeyCode(char='z'):
        pyautogui.keyDown('ctrlleft')
        pressKeys('d','s','w','w','a','s')
        pyautogui.keyUp('ctrlleft')
    #Resupply
    elif key == Key.f1:
        pyautogui.keyDown('ctrlleft')
        pressKeys('s','s','w','d')
        pyautogui.keyUp('ctrlleft')
    #Runbler
    elif key == Key.f2:
        pyautogui.keyDown('ctrlleft')
        pressKeys('s','a','w','a','a')
        pyautogui.keyUp('ctrlleft')
    #Jump Pack
    elif key == Key.f3:
        pyautogui.keyDown('ctrlleft')
        pressKeys('s','w','w','s','w')
        pyautogui.keyUp('ctrlleft')
    #Drone
    elif key == Key.f4:
        pyautogui.keyDown('ctrlleft')
        pressKeys('a','w','d')
        pyautogui.keyUp('ctrlleft')
    #Meltal Detector
    elif key == Key.f5:
        pyautogui.keyDown('ctrlleft')
        pressKeys('s','s','d','w')
        pyautogui.keyUp('ctrlleft')
        
def handleRelease(key):
    #print( 'Released: {}'.format( key ) )
    if key == Key.esc:
        return False

if __name__ == "__main__":
    print('\nESC : quit mecro\n')
    print('F : Reinforce')
    print('V : Railcannon Strike')
    print('C : Heavy Airstrike')
    print('X : Shredder Missile Strike')
    print('Z : Thunderer Barrage')
    print('F1 : Resupply')
    print('F2 : Runbler')
    print('F3 : Jump Pack')
    print('F4 : Drone')
    print('F5 : Meltal Detector')
    with Listener(on_press=handlePress, on_release=handleRelease) as listener:
        listener.join()