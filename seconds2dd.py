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

# seconds = sys.argv[1]
# if(len(sys.argv) < 3):
#     hoursPerDay = 7.5
# else:
#     hoursPerDay = sys.argv[2]

# response = ddhhmmss(seconds, hoursPerDay)
# print('{"items": [{"title":"'+response+'", "subtitle": "DD:HH:MM:SS"}]}')