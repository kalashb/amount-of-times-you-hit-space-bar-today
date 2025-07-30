from pynput import keyboard

# Change this to the key you want to count
TARGET_KEY = keyboard.Key.space  # For spacebar
# For a letter, use: TARGET_KEY = 'a'

count = 0

def on_press(key):
    global count
    # For special keys (like spacebar, enter, etc.)
    if key == TARGET_KEY:
        count += 1
        print(f"{TARGET_KEY} pressed {count} times")
    # For letter/number keys (uncomment below and set TARGET_KEY = 'a', etc.)
    # try:
    #     if key.char == TARGET_KEY:
    #         count += 1
    #         print(f\"'{TARGET_KEY}' pressed {count} times\")
    # except AttributeError:
    #     pass

with keyboard.Listener(on_press=on_press) as listener:
    print("Press keys. Press Ctrl+C to exit.")
    listener.join()