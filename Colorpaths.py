import RandomFunctions


def straightline(numloops, rgb_start, rgb_end):
    '''
    Returns a 'numloops'-long list of 3-element lists of RGB values (RGB triples)
    in that order.  The RGB values are equally spaced (to the next lowest integer)
    along a straight line connecting the start and end points in RGB space.

    Args:
        (int) numloops - the length of the list of RGB triples
        (tuple or list of int) rgb_start - the starting point in RGB space
        (tuple or list of int) rgb_end - the ending point in RGB space

    Returns:
        (list of 3-element lists of int) rgb_list

    >>> numloops, rgb_start, rgb_end = 5, (0, 0, 0), (100, 100, 100)
    >>> straightline(numloops, rgb_start, rgb_end)
    [[0, 0, 0], [25, 25, 25], [50, 50, 50], [75, 75, 75], [100, 100, 100]]

    >>> numloops, rgb_start, rgb_end = 5, (0, 0, 0), (100, 0, 0)
    >>> straightline(numloops, rgb_start, rgb_end)
    [[0, 0, 0], [25, 0, 0], [50, 0, 0], [75, 0, 0], [100, 0, 0]]

    >>> numloops, rgb_start, rgb_end = 5, (0, 0, 0), (0, 100, 0)
    >>> straightline(numloops, rgb_start, rgb_end)
    [[0, 0, 0], [0, 25, 0], [0, 50, 0], [0, 75, 0], [0, 100, 0]]

    >>> numloops, rgb_start, rgb_end = 5, (0, 0, 0), (0, 0, 100)
    >>> straightline(numloops, rgb_start, rgb_end)
    [[0, 0, 0], [0, 0, 25], [0, 0, 50], [0, 0, 75], [0, 0, 100]]

    >>> numloops, rgb_start, rgb_end = 4, (0, 0, 0), (1, 1, 1)
    >>> straightline(numloops, rgb_start, rgb_end)
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 1, 1]]

    >>> numloops, rgb_start, rgb_end = 4, (0, 0, 0), (0, 0, 0)
    >>> straightline(numloops, rgb_start, rgb_end)
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
    '''

    x = [0,0,0]  # Intialize the rgb vector

    r, g, b = x[0], x[1], x[2] = rgb_start
    end_r, end_g, end_b = rgb_end

    Rinterval = (end_r - r)/(numloops - 1)
    Ginterval = (end_g - g)/(numloops - 1)
    Binterval = (end_b - b)/(numloops - 1)

    #print('RGB Intervals: ', Rinterval, Ginterval, Binterval)

    rgb_list = [ [r, g, b] ]

    for i in range(1, numloops):
        x[0] += Rinterval
        x[1] += Ginterval
        x[2] += Binterval

        r, g, b = int(x[0]), int(x[1]), int(x[2])

        rgb_list.append([r, g, b])


    return rgb_list


def Manhattan(numloops, rgb_start, rgb_end, rgb_order):
    '''
    Returns a 'numloops'-long list of 3-element lists of RGB values (RGB triples)
    in that order.  The RGB values are equally spaced (to the next lowest integer)
    along a path that closes the distance in RGB space between the start and end
    points by following a "Manhattan" path, a path that proceeds along one dimension,
    then another, and then the remaining one.  The order of the dimensions is
    determined by the 'rgb_order'.

    Args:
        (int) numloops - the length of the list of RGB triples
        (tuple or list of int) rgb_start - the starting point in RGB space
        (tuple or list of int) rgb_end - the ending point in RGB space
        (str) rgb_order - the order of the dimesions for the path through RGB space

    Returns:
        (list of 3-element lists of int) rgb_list


    >>> numloops, rgb_start, rgb_end, rgb_order = 5, (0, 0, 0), (100, 0, 0), 'RGB'
    >>> Manhattan(numloops, rgb_start, rgb_end, rgb_order)
    [[0, 0, 0], [25, 0, 0], [50, 0, 0], [75, 0, 0], [100, 0, 0]]

    >>> numloops, rgb_start, rgb_end, rgb_order = 5, (0, 0, 0), (0, 100, 0), 'RGB'
    >>> Manhattan(numloops, rgb_start, rgb_end, rgb_order)
    [[0, 0, 0], [0, 25, 0], [0, 50, 0], [0, 75, 0], [0, 100, 0]]

    >>> numloops, rgb_start, rgb_end, rgb_order = 5, (0, 0, 0), (0, 0, 100), 'RGB'
    >>> Manhattan(numloops, rgb_start, rgb_end, rgb_order)
    [[0, 0, 0], [0, 0, 25], [0, 0, 50], [0, 0, 75], [0, 0, 100]]

    >>> numloops, rgb_start, rgb_end, rgb_order = 5, (0, 0, 0), (100, 0, 0), 'BGR'
    >>> Manhattan(numloops, rgb_start, rgb_end, rgb_order)
    [[0, 0, 0], [25, 0, 0], [50, 0, 0], [75, 0, 0], [100, 0, 0]]

    >>> numloops, rgb_start, rgb_end, rgb_order = 4, (0, 0, 0), (100, 100, 100), 'RGB'
    >>> Manhattan(numloops, rgb_start, rgb_end, rgb_order)
    [[0, 0, 0], [100, 0, 0], [100, 100, 0], [100, 100, 100]]
    
    >>> numloops, rgb_start, rgb_end, rgb_order = 4, (0, 0, 0), (100, 100, 100), 'RBG'
    >>> Manhattan(numloops, rgb_start, rgb_end, rgb_order)
    [[0, 0, 0], [100, 0, 0], [100, 0, 100], [100, 100, 100]]

    >>> numloops, rgb_start, rgb_end, rgb_order = 4, (0, 0, 0), (100, 100, 100), 'GRB'
    >>> Manhattan(numloops, rgb_start, rgb_end, rgb_order)
    [[0, 0, 0], [0, 100, 0], [100, 100, 0], [100, 100, 100]]

    >>> numloops, rgb_start, rgb_end, rgb_order = 4, (0, 0, 0), (100, 100, 100), 'GBR'
    >>> Manhattan(numloops, rgb_start, rgb_end, rgb_order)
    [[0, 0, 0], [0, 100, 0], [0, 100, 100], [100, 100, 100]]

    >>> numloops, rgb_start, rgb_end, rgb_order = 4, (0, 0, 0), (100, 100, 100), 'BRG'
    >>> Manhattan(numloops, rgb_start, rgb_end, rgb_order)
    [[0, 0, 0], [0, 0, 100], [100, 0, 100], [100, 100, 100]]

    >>> numloops, rgb_start, rgb_end, rgb_order = 4, (0, 0, 0), (100, 100, 100), 'BGR'
    >>> Manhattan(numloops, rgb_start, rgb_end, rgb_order)
    [[0, 0, 0], [0, 0, 100], [0, 100, 100], [100, 100, 100]]

    >>> numloops, rgb_start, rgb_end, rgb_order = 5, (0, 0, 0), (100, 100, 100), 'RGB'
    >>> Manhattan(numloops, rgb_start, rgb_end, rgb_order)
    [[0, 0, 0], [75, 0, 0], [100, 50, 0], [100, 100, 25], [100, 100, 100]]

    '''

    ### Color Evolution Initialization -----------------

    mapping = {'RGB': '012',
               'RBG': '021',
               'GRB': '102',
               'GBR': '120',
               'BRG': '201',
               'BGR': '210'}

    # Create indices for ijk space corresponding to rgb space
    i = int(mapping[rgb_order][0])
    j = int(mapping[rgb_order][1])
    k = int(mapping[rgb_order][2])

    x = [0,0,0]  # Initialize the rgb vector
    r, g, b = x[0], x[1], x[2] = rgb_start
    # Create corresponding ijk vectors
    # for i, j, k ordered path through rgb space
    z = [x[i], x[j], x[k]]
    ijk_start = [rgb_start[i], rgb_start[j], rgb_start[k]]
    ijk_end = [rgb_end[i], rgb_end[j], rgb_end[k]]

    # Calculate Manhattan distance (Mdist) through RGB color space
    # and step size for each iteration (Minterval)
    Mdist = (
            abs(rgb_end[0] - r) +
            abs(rgb_end[1] - g) + 
            abs(rgb_end[2] - b)
            )
    #print(f'Mdist is: {Mdist}')
    Minterval = Mdist/(numloops - 1)
    #print(f'Minterval is: {Minterval}')


    rgb_list = [ [r, g, b] ]

    sign = lambda x: -1 if x<0 else 1

    sign_0 = sign(ijk_end[0] - ijk_start[0])
    sign_1 = sign(ijk_end[1] - ijk_start[1])
    sign_2 = sign(ijk_end[2] - ijk_start[2])
    dist_0 = abs(ijk_end[0] - ijk_start[0])
    dist_1 = abs(ijk_end[1] - ijk_start[1])
    dist_2 = abs(ijk_end[2] - ijk_start[2])

    for m in range(1, numloops):
        dist_traveled = m * Minterval

        if dist_traveled <= dist_0:
            z[0] = ijk_start[0] + sign_0 * dist_traveled
        elif dist_0 < dist_traveled <= (dist_0 + dist_1):
            z[0] = ijk_end[0]
            z[1] = ijk_start[1] + sign_1 * (dist_traveled - dist_0)
        else:
            z[0] = ijk_end[0]
            z[1] = ijk_end[1]
            z[2] = ijk_start[2] + sign_2 * (dist_traveled - dist_0 - dist_1)

        # Update the rgb vector --> x
        x[i], x[j], x[k] = z[0], z[1], z[2]

        # Obtain integer values from the rgb vector
        r, g, b = int(x[0]), int(x[1]), int(x[2])  
        
        rgb_list.append([r, g, b])

    return rgb_list

def randomwalk(numloops, rgb_start, noise_interval_size):
    rgb = list(rgb_start)
    print('RGB start: ', rgb)
    rgb_list = [rgb]
    print('Start RGB list: ', rgb_list)
    for i in range(1, numloops):
        new_rgb = rgb_list[-1].copy()
        new_rgb = RandomFunctions.random_select(new_rgb, noise_interval_size)
        rgb_list.append(new_rgb)

    return rgb_list


def rainbowpath(numloops, rgb_locations):
    num_locations = len(rgb_locations)
    num_legs = num_locations - 1

    leg_length = numloops//num_legs
    travel_delay = numloops%num_legs        # Remainder loops
    
    # Create rgb_list
    delay_list = [rgb_locations[0].copy()] * travel_delay   # Add remainder loops to the start
    rgb_list = delay_list

    for i in range(0, num_legs):
        leg_list = straightline(leg_length, rgb_locations[i], rgb_locations[i+1])
        rgb_list += leg_list.copy()

    # Return rgb_list
    return rgb_list


def randompath(numloops, rgb_start, rgb_end):
    num_stopovers = 3

    # Create list of random stopovers
    stopovers = [[0, 0, 0].copy() for i in range(num_stopovers)]

    for i in range(num_stopovers):
        stopovers[i] = RandomFunctions.random_select(stopovers[i], 256)
    
    # Create list of total locations

    locations = [list(rgb_start)] + stopovers + [list(rgb_end)]

    #print("Locations: ", locations)

    rgb_list = rainbowpath(numloops, locations)
    
    # Return rgb_list
    return rgb_list



###################
### For Testing ###
###################

if __name__ == '__main__':
    import doctest
    doctest.testmod()


###########################################
####### For Testing randomwalk
##
##numloops = 5
##rgb_start = (244, 0, 100)
##noise_interval_size = 64
##
##rgb_list = randomwalk(numloops, rgb_start, noise_interval_size)
##
##print(rgb_list)

###########################################
####### For Testing randompath
##
##numloops = 30
##rgb_start = (0,0,0)
##rgb_end = (255, 255, 255)
##
##rgb_list = randompath(numloops, rgb_start, rgb_end)
##
##print(rgb_list)


