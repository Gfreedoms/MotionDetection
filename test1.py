import os
import sys
import time
def test():
    while True:
        status = "off"
        executable = sys.executable
        args = sys.argv[:]
        args.insert(0, sys.executable)
        time.sleep(3)
        #while True:
        if status == "on":
            print ("yes")
        else:
            continue
            #print("")
        os.execvp(executable, args)
if __name__ == "__main__":
    test()