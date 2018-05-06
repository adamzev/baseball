''' general math equations for rocket simulations '''
import math

ACCEL_OF_GRAVITY = 32.17405


def myround(x, base=50):
    ''' rounds numbers to the nearest multiple of a given base '''
    return int(base * round(float(x) / base))


def mphToFps(mph):
    return 5280.0 * mph / (60.0 * 60.0)


def fpsToMph(fps):
    return fps * (60.0 * 60.0) / 5280.0


def average_list(values):
    return sum(values) / float(len(values))


def average(*args):
    args = [x for x in args if x is not None]
    # args = filter(None, args)   removes both zeros and None
    return sum(args) / float(len(args))


def pythag(a, b, c=None):
    if (a is None and b is None) or (a is None and c is None) or (b is None and c is None):
        return None

    if c is None:
        return float(math.sqrt(a**2 + b**2))
    if a is None:
        hyp = c
        given_leg = b
    if b is None:
        hyp = c
        given_leg = a
    return float(math.sqrt(hyp**2 - given_leg**2))
