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
            elif code == 26:
                print("Restarting Bot.")
                continue

    print("Bot has been terminated. Exit code: %d" % code)

if __name__ == '__main__':
    print("Running bot from launcher.")
    run_bot()
