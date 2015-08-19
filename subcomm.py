#!/usr/bin/env python

""" Execute commands and args specified as args to the script.
Catch stdout and stdin and do a regex on them printing result.
"""

from subprocess import Popen
from subprocess import PIPE
from StringIO import StringIO
import time
import sys
import re

def main(args):
    pattern=r"""
            (\w*)\s*    # group1
            (\w*)       # group2
            """
    regex = re.compile(pattern, re.X)
    proc = Popen(args, stdout=PIPE, stderr=PIPE)
    stdout, stderr = proc.communicate()
    s = StringIO(stdout)
    while s.tell() < s.len:
        line = s.readline().strip()
        print line
        g1, g2 = regex.search(line).group(1,2)
        print "%r %r" % (g1, g2)

if __name__ == '__main__':
    main(sys.argv[1:])
