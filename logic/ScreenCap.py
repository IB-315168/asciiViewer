from pynput import mouse


class ScreenCap:
    #TODO refactor as an array
    xPos1 = 0
    yPos1 = 0
    complete = False

    xPos2 = 0
    yPos2 = 0


def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))


def on_click(x, y, button, pressed):
    if pressed:
        ScreenCap.xPos1 = x
        ScreenCap.yPos1 = y
    else:
        ScreenCap.xPos2 = x
        ScreenCap.yPos2 = y
        ScreenCap.complete = True
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))



def on_scroll(x, y, dx, dy):
    print('Scrolled {0}'.format(
        (x, y)))


# Collect events until released
listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)
