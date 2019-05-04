import sys

def ddhhmmss(seconds, hours=7.5):
    """Convert seconds to a time string "[[[DD:]HH:]MM:]SS".
    """
    hours = float(hours)
    secondsPerDay = int(hours*3600)
    dhms = ''
    for scale in secondsPerDay, 3600, 60:
        result, seconds = divmod(int(seconds), int(scale))
        # if dhms != '' or result > 0:
        dhms += '{0:02d}:'.format(result)
    dhms += '{0:02d}'.format(seconds)
    return dhms

def parseValue(value):
    humanStrings = [' day', ' hour', ' minute', ' second']
    humanStrings.reverse()
    ret = ''
    for segment in value.split(":"):
        if segment == "00":
            continue

        ret += segment.lstrip("0")+humanStrings.pop()
        if int(segment) > 1:
            ret += "s"
        ret +=", "

    return ret.rstrip(", ")