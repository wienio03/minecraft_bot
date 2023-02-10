import pyautogui as ag
from time import sleep

def nav_to_image(image, clicks, off_x=0, off_y=0):
    position = ag.locateCenterOnScreen(image, confidence=0.7)
    if position is None:
        print(f'{image} not found')
        return 0
    else:
        ag.moveTo(position, duration=0.1)
        ag.moveRel(off_x, off_y)
        ag.click(clicks=clicks, interval=0.3)

    # move the character
    # x = attack
    # c = place
def move_character(key_press, duration, action='walking'):
        ag.keyDown(key_press)

        if action == 'walking':
             print('walking')
        elif action == 'attack':
             ag.keyDown('x')

        sleep(duration)
        ag.keyUp('x')
        ag.keyUp(key_press)

def locate_lava():
    position = ag.locateCenterOnScreen('images/lava.png', confidence=0.5)

    if position is None:
        return False
    else:
        move_character('s', 2)
        print('Lava has been found!!!!')
        return True


    #zacznij gre
sleep(5)
nav_to_image('images/start_game.png', 3)

duration = 10
while duration != 0:

    #if no lava, continue
    if not locate_lava():
        move_character('w', 2, 'attack')
    else:
        break

    duration -= 1

    print('time left = ', duration)






