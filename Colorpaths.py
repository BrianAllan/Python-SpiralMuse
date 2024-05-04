
def straightline(numloops, rgb_start, rgb_end):

    x = [0,0,0]  # Intialize the rgb vector

    r, g, b = x[0], x[1], x[2] = rgb_start
    end_r, end_g, end_b = rgb_end

    Rinterval = (end_r - r)/numloops
    Ginterval = (end_g - g)/numloops
    Binterval = (end_b - b)/numloops

    print('RGB Intervals', Rinterval, Ginterval, Binterval)

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

    mapping = {'rgb': '012',
               'rbg': '021',
               'grb': '102',
               'gbr': '120',
               'brg': '201',
               'bgr': '210'}

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

##############################################################
#### For Testing

#rgb_list = straightline(360, (0,0,0), (255, 255, 255))
rgb_list = Manhattan(360, (0,0,0), (255, 255, 255), 'rgb')

print('List length: ', len(rgb_list), '\nHead: ', rgb_list[:5], '\nTail: ', rgb_list[-5:])
