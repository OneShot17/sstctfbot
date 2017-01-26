#!/usr/bin/env python3

import sys
import subprocess

def run_bot():
    interpreter = sys.executable
    cmd = (interpreter, "bot.py")

    while True:
        try:
            code = subprocess.call(cmd)
        except KeyboardInterrupt:
            code = 0
            break
        else:
            if code == 0:
                break
            elif code == 2:
                print("Bot does not exist.")
                break
            elif code == 25:
                print("Restarting and updating Bot.")
                update_bot()
                continue
            elif code == 26:
                print("Restarting Bot.")
                continue

    print("Bot has been terminated. Exit code: %d" % code)

def update_bot():
    try:
        code = subprocess.call(("git", "pull", "--ff-only"))
    except FileNotFoundError:
        print("Error: Git not found.")
        return
    if code == 0:
        print("Bot has been updated.")
    else:
        print("Bot could not be updated properly.")

if __name__ == '__main__':
    print("Running bot from launcher.")
    run_bot()
