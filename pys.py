import traceback, sys

def magic():
    while True:
        cmd = sys.stdin.readline()
        if not cmd:
            continue
        try:
            exec(cmd)
        except Exception as err:
            if isinstance(err, KeyboardInterrupt):
                break
            traceback.print_last()

magic()