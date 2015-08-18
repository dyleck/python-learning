import os
import sys
import time
import random

def main():
    LEVEL = ['ERROR','DEBUG','INFO']
    OBJECTS = ['obj1', 'obj2', 'obj3', 'obj4', 'obj5']
    DIFF = ['THIS','THAT']
    
    for i in range(1,5):
        for f in range(0,1000):
            try:
                fsock = open("app.log." + str(i), "a", 0)
            except IOError:
                sys.exit(1)
            tm  = time.strftime("%Y-%m-%d %H:%M", time.localtime(time.time() + random.randint(0,1000)))
            prTime = random.randint(0,10000)
            line = "{0} {1} {2} object: {3} processing: {4}".format(tm,
                                                                    random.choice(LEVEL),
                                                                    random.choice(DIFF),
                                                                    random.choice(OBJECTS),
                                                                    prTime)
            fsock.write(line + "\n")
        fsock.close()

if __name__ == '__main__':
    main()