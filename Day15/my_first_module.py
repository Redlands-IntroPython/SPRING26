# Solution to Practice Problems Day 15
# my_first_module.py

def calcuate_tip(total,tip_percent):
    ''' Calculates a tip from a percent
        Expectes percent as an integer.'''
    # Check percent is an integer
    if type(tip_percent) == type(1):
        tip = total*tip_percent/100
    else:
        print('The percent should be an integer value between 0 and 100')
    return tip


def split_bill(num_p, total, tip):
    '''Splits a bill between num_p people '''
    bill = total+tip
    cost_per = bill/num_p
    return cost_per

