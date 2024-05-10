import RandomFunctions


def straightline(numloops, rgb_start, rgb_end):

    x = [0,0,0]  # Intialize the rgb vector

    r, g, b = x[0], x[1], x[2] = rgb_start
    end_r, end_g, end_b = rgb_end

    Rinterval = (end_r - r)/(numloops - 1)
    Ginterval = (end_g - g)/(numloops - 1)
    Binterval = (end_b - b)/(numloops - 1)

    #print('RGB Intervals', Rinterval, Ginterval, Binterval)

    rgb_list = [ [r, g, b] ]

    for i in range(1, numloops):
        x[0] += Rinterval
        x[1] += Ginterval
        x[2] += Binterval

        r, g, b = int(x[0]), int(x[1]), int(x[2])

        rgb_list.append([r, g, b])


    return rgb_list


def Manhattan(numloops, rgb_start, rgb_end, rgb_order):

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
    ijk_end = [rgb_end[i], rgb_end[j], rgb_end[k]]

    # Calculate Manhattan distance (Mdist) through RGB color space
    # and step size for each iteration (Minterval)
    Mdist = (
            abs(rgb_end[0] - r) +
            abs(rgb_end[1] - g) + 
            abs(rgb_end[2] - b)
            )
    print(f'Mdist is: {Mdist}')
    Minterval = Mdist/numloops
    print(f'Minterval is: {Minterval}')


    rgb_list = [ [r, g, b] ]

    for m in range(1, numloops):
        # Evolve the ijk vector --> z
        if z[0] - ijk_end[0] > Minterval/2:
            z[0] -= Minterval
        elif ijk_end[0] - z[0] > Minterval/2:
            z[0] += Minterval
        elif z[1] - ijk_end[1] > Minterval/2:
            z[1] -= Minterval
        elif ijk_end[1] - z[1] > Minterval/2:
            z[1] += Minterval
        elif z[2] - ijk_end[2] > Minterval/2:
            z[2] -= Minterval
        elif ijk_end[2] - z[2] > Minterval/2:
            z[2] += Minterval
        else:
            pass

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

    
    

##############################################################
#### For Testing straightline and Manhattan

##rgb_list = straightline(10, (0,0,0), (50, 50, 50))
##rgb_list = Manhattan(360, (0,0,0), (255, 255, 255), 'rgb')

##print('List length: ', len(rgb_list), '\nHead: ', rgb_list[:5], '\nTail: ', rgb_list[-5:])


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


