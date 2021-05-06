import numpy as np

def check_empty_input(current_ranges):
    if len(current_ranges) == 0:
        return 'Empty_Input'
    return True

def check_is_nan(current_rages):
    if np.isnan(current_rages):
        return 'Valid Input'
    return False
  
