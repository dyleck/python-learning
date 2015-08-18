import re
import sys


class Object():
    def __init__(self, name, count, ptime):
        self.name = name
        self.count = count
        self.ptime = int(ptime)
        self.avg = 0

    def average_time(self):
        return self.ptime / self.count

    def __str__(self):
        return "{0}: count: {1} avg: {2}".format(self.name,
                                                 self.count,
                                                 self.average_time())


def main():
    pattern = """
        \d{4}-\d{2}-\d{2}
        \s*
        \d{2}:\d{2}
        \s*
        (\w*)
        \s
        (\w*)
        \s
        object:\s(\w*)\sprocessing:\s(\d*)
        """
    regex = re.compile(pattern, re.VERBOSE)
    dict = {}
    try:
        fsock = open("app.log.1", "r", 0)
        for line in fsock:
            res = regex.match(line)
            if res:
                level, desc, obj, ptime = res.group(1, 2, 3, 4)
                if level == "ERROR" and desc == "THIS":
                    try:
                        o = dict[obj]
                        o.count += 1
                        o.ptime += int(ptime)
                    except KeyError:
                        dict[obj] = Object(obj, 1, ptime)
    except IOError:
        print "Error"
        sys.exit(1)
    finally:
        fsock.close()
    for v in dict.values():
        print v


if __name__ == '__main__':
    main()
