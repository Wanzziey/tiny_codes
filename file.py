import keyboard
import time

x = input('ile iteracji: ')
x = int(x)
print('ustaw')
time.sleep(5)

for i in range(x):
    print(i)
    keyboard.press('ctrl')
    keyboard.press('q')
    keyboard.release('q')
    keyboard.release('ctrl')
    keyboard.press('enter')
    keyboard.release('enter')
#opcjonalnie
    keyboard.press('enter')
    keyboard.release('enter')
    #keyboard.press_and_release('down') przeskok w spisie
    
    keyboard.press('ctrl')
    keyboard.press_and_release('page down')
    keyboard.release('ctrl')
    keyboard.press_and_release('down')  #przeskok w bazie
    
