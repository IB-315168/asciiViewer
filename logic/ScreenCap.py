from pynput import mouse


class ScreenCap:
    pos = [0, 0, 0, 0]
    complete = False


def on_click(x, y, button, pressed):
    if pressed:
        ScreenCap.pos[0] = x
        ScreenCap.pos[1] = y
    else:
        ScreenCap.pos[2] = x
        ScreenCap.pos[3] = y
        ScreenCap.complete = True
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
