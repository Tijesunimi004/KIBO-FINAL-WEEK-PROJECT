from time import sleep

def animate(string, time=0.1):
    current = ""
    for char in string: 
        # Extend the current string by this character
        current += char

        # Insert a carriage return before printing and flush immediately
        print(f"\r{current}", end="", flush=True)

        # Sleep for a specified amount of time
        sleep(time)