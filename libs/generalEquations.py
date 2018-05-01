''' general math equations for rocket simulations '''
import math

ACCEL_OF_GRAVITY = 32.17405

def myround(x, base=50):
    ''' rounds numbers to the nearest multiple of a given base '''
    return int(base * round(float(x)/base))

def percentOfAtmosphericPressure(alt):
    ''' Take the altitude and returns the percent of atmospheric pressure
        "alt" is altitude in feet from the surface of earth
    '''

    #where sea level PATM = 1.00 and vacuum PATM = 0.00; altitude given in feet
    #1
    if alt <= 36089:
        patm = (1.0 - (alt/145442.0)) ** 5.255877122
    #2
    elif alt <= 65617: #(11 km to 20 km)
    # where 'math.exp' is exponential function 'e' raised to the 'x' power
        patm = 0.223361 * math.exp((36089.0 - alt)/20806.0)
    #3
    elif alt <= 104987: #(20 km to 32 km)
        patm = (0.988626 + (alt / 652600.0)) ** (-34.16319)
    #4
    elif alt <= 154199: #(32 km to 47 km)
        patm = (0.898309 + (alt / 181373.0)) ** (-12.20114)
    #5
    elif alt <= 167323: #(47 km to 51 km)
        patm = 0.00109456 * math.exp((alt - 154200)/-25992.0)
    #6
    elif alt <= 232940: #(51 km to 71 km)
        patm = (0.838263 - (alt / 577922.0)) ** (12.20114)
    #7
    elif alt <= 278386: #(71 km to 84.852 km)
        patm = (0.917131 - (alt / 637919.0)) ** (17.08160)
    #8
    else: #for alt> 84.852
        return 0.00
    return patm

def percentOfVac(alt):
    ''' Takes the altitude and returns the percent of vacuum (1 - atmospheric pressure)'''
    return 1.0 - percentOfAtmosphericPressure(alt)

def orbitalVelocity(alt):
    return 17683.9567 * ((1.0 / (1.0 + (alt / 20902230.99)))** 0.5)

def mphToFps(mph):
    return 5280.0*mph/(60.0*60.0)

def fpsToMph(fps):
    return fps*(60.0*60.0)/5280.0

def average_list(values):
    return sum(values)/float(len(values))

def average(*args):
    args = [x for x in args if x is not None]
    # args = filter(None, args)   removes both zeros and None
    return sum(args)/float(len(args))

def pythag(a, b, c = None):
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

def ADC(air_speed_mph, alt, K):
    return ((air_speed_mph / 1000.0)**2.0) * percentOfAtmosphericPressure(alt) * K  # with resultant ADC in  "g" units

def altitude(alt_prev, V_vert_prev, V_vert_inc, time_inc):
    return alt_prev + V_vert_prev * time_inc + (V_vert_inc * time_inc) / 2.0

def bigG(horizontalVelocity, orbitalV):
    ''' "G" is downward (vertical) acceleration: Earth's gravity minus centrifugal force
        caused by horizontal velocity (V H )
    '''
    big_g = 1 - ((horizontalVelocity / orbitalV)**2)
    if big_g > 0.0:
        return big_g
    else:
        return 0.0
