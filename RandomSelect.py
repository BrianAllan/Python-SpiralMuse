
import random

def noisy_list(rgb_list, noise_interval_size):
    s = int(noise_interval_size/2)
    for rgb in rgb_list:
        for i in range(0,3):
            low_end = rgb[i] - s
            high_end = rgb[i] + s

            if low_end < 0:
                hi = high_end + abs(low_end)
                high_end = hi if (hi <= 255) else 255
                low_end = 0
            if high_end > 255:
                lo = low_end + (255 - high_end)
                low_end = lo if (lo >= 0) else 0
                high_end = 255

            rgb[i] = random.randint(low_end, high_end)

    return rgb_list


########## for Testing
##
##import random
##
##interval_size = 5
##
##start = [0, 50, 100]
##
##rgb_list = []
##
##for i in range(0, 40):
##    temp_list = [start[0] + i, start[1] + i, start[2] + i]
##    rgb_list.append(temp_list)
##
##print('Initial list: \n', rgb_list)
##
##
##print('Randomized: \n', noisy_list(rgb_list, interval_size) )
            
        
