# import library

import numpy as np
import shapely.geometry as sg
import geopandas as gpd
from shapely.geometry import shape
from shapely.geometry import Point

# rhombic point sequences function
def init_rhomb_seq(point_init, sidelength, cols):
    """Generates a rhombic sequence of points for a Cartesian planar diagram.

    Parameter:
        point_init: A list of x and y coordinates
        sidelength: The number of sidelength will be generated
        rows: the number of rows will be generated

    Returns:
        A list of shapely Point objects.
    """
    if sidelength <= 0:
        raise ValueError("sidelength must be greater than zero")
    
    sequence_xy = []
    x_init = point_init[0] 
    y_init = point_init[1]
    
    for i in range(cols):
        x = i * 1.5 * sidelength
        y = i*np.sqrt(3)*1.5 * sidelength
        x_n = -x
        y_offset = []
        for a in range (cols - i):
            if (a + i) % 2 == 0:
                y_new = a * np.sqrt(3)/2 * sidelength
                y_offset.append(y_new)
        
        for _,j in enumerate(y_offset):
            sequence_xy.append((x_init + x, y_init + j))    # 1
            sequence_xy.append((x_init - x, y_init - j))    # 2
            sequence_xy.append((x_init + x_n, y_init + j))  # 3
            sequence_xy.append((x_init - x_n, y_init - j))  # 4
            
    seq_rhomb = [Point(x, y) for (x, y) in sequence_xy] 
    return seq_rhomb

def init_rhomb_seqv(point_init, sidelength, cols):
    """Generates a rhombic sequence of points on Cartesian planar diagram.

    Parameter:
        point_init: A list of x and y coordinates
        sidelength: The number of sidelength will be generated
        rows: the number of rows will be generated

    Returns:
        A list of shapely Point objects.
    """
    if sidelength <= 0:
        raise ValueError("sidelength must be greater than zero")
    
    sequence_xy = []
    x_init = point_init[0] 
    y_init = point_init[1]
    
    for i in range(cols):
        x = i * np.sqrt(3)/2 * sidelength
        y = i*np.sqrt(3)*1.5 * sidelength
        x_n = -x
        y_offset = []
        for a in range (cols - i):
            if (a + i) % 2 == 0:
                y_new = a * 1.5 * sidelength
                y_offset.append(y_new)
        
        for _,j in enumerate(y_offset):
            sequence_xy.append((x_init + x, y_init + j))    # 1
            sequence_xy.append((x_init - x, y_init - j))    # 2
            sequence_xy.append((x_init + x_n, y_init + j))  # 3
            sequence_xy.append((x_init - x_n, y_init - j))  # 4
            
    seq_rhomb_v = [Point(x, y) for (x, y) in sequence_xy] 
    return seq_rhomb_v

def init_rect_seq(point_init, sidelength, cols, rows):
    """
    Generates a rectangular sequence of points on Cartesian planar diagram.

    Parameter:
        point_init: A list of x and y coordinates
        sidelength: The number of sidelength will be generated
        rows: the number of rows will be generated
        cold: the number of columns will be generated

    Returns:
        A list of shapely Point objects.
    """
    if sidelength <= 0:
        raise ValueError("sidelength must be greater than zero")

    sequence_xy = []
    
    # x_init, y_init = point_init[0], point_init[1]
    x_init = point_init[0] 
    y_init = point_init[1]

    for num_x in range(cols):
    # initiate iteration for x in num_x
        x_new = x_init + (1.5 * sidelength*num_x)
        for num_y in range(rows):
            if ((num_x + 1)  % 2) == 0:
            # condition where column number (num_x + 1) is odd number
                y_new = y_init + ((3**0.5)*sidelength*num_y)
                point = (x_new,y_new)
            else:
            # condition where column number (num_x + 1) is even number
                y_new = (y_init + ((3**0.5)*sidelength*num_y)) - (0.5* (3**0.5)*sidelength)
                point = (x_new,y_new)

        sequence_xy.append(point)

    seq_rectangular = [Point(x, y) for (x, y) in sequence_xy]
    return seq_rectangular

def init_rect_seqv(point_init, sidelength, cols, rows):
    """
    Generates a rectangular sequence of points on Cartesian planar diagram.

    Parameter:
        point_init: A list of x and y coordinates
        sidelength: The number of sidelength will be generated
        rows: the number of rows will be generated
        cold: the number of columns will be generated

    Returns:
        A list of shapely Point objects.
    """
    sequence_xy_v = [] # an empty list
    
    # x_init, y_init = point_init[0], point_init[1]
    x_init = point_init[0] 
    y_init = point_init[1]

    for num_y in range(rows):
        y_new = y_init + (1.5 * sidelength*num_y)
        for num_x in range(cols):
            if ((num_y + 1)  % 2) == 0:
                # condition where row number (num_x + 1) is odd number
                x_new = x_init + ((3**0.5)*sidelength*num_x)
                point = (x_new,y_new)
            else: # condition where row number (num_x + 1) is even number
                x_new = (x_init + ((3**0.5)*sidelength*num_x)) - (0.5* (3**0.5)*sidelength)
                point = (x_new,y_new)

    sequence_xy_v.append(point)
    seq_rect_v = [Point(x, y) for (x, y) in sequence_xy_v]
    return seq_rect_v

# generate hexagon function
def hex (sidelength, x_init, y_init):
    '''
    function to generate equillateral horizontal hexagon shape
    Parameter:
    - s: (int/float) sidelength of the hexagon shape
    - x_init: (int/float) x coordinate of the hexagon to be initiated
    - y_init: (int/float) y coordinate of the hexagon to be initiated
    '''
    # initiate theta of equilateral hexagon, which is 120 degrees
    int_angle = 2*np.pi/3 

    #initiate an empty list
    coor_list = []

    # initiate first state of integer variable for looping purposes
    a = 0
    point_x = x_init
    point_y = y_init

    # do the loop for coordinate plotting
    while a < 6: 
        # state a first theta, and repeat by a += 1
        theta = a * int_angle
        a += 1

        # calculate x and y variable 
        x = sidelength*(np.cos(theta)) + point_x
        y = sidelength*(np.sin(theta)) + point_y
        
        
        # state a conditional statements on loop in even numbers
        if a % 2 == 0:
            x = sidelength*(np.cos(theta))*(-1) + point_x
            y = sidelength*(np.sin(theta))*(-1) + point_y
        
        # put all of the output to coor_list variable
        coor_list.append((x,y))

    # convert coor_list into array
    coord = np.array(coor_list)
        
    # calculate area and plot hexagon with coord variable
    area = (np.sqrt(3)/2)*(s**2)
    hexagon = sg.Polygon(coord)
    return hexagon

# generate hexagon function
def hex_v (sidelength, x_init, y_init):
    '''
    function to generate equillateral vertical hexagon shape
    Parameter:
    - s: (int/float) sidelength of the hexagon shape
    - x_init: (int/float) x coordinate of the hexagon to be initiated
    - y_init: (int/float) y coordinate of the hexagon to be initiated
    '''
    # initiate theta of equilateral hexagon, which is 120 degrees
    int_angle = 2*np.pi/3 

    #initiate an empty list
    coor_list = []

    # initiate first state of integer variable for looping purposes
    a = 0
    point_x = x_init
    point_y = y_init

    # do the loop for coordinate plotting
    while a < 6: 
        # state a first theta, and repeat by a += 1
        theta = a * int_angle
        a += 1

        # calculate x and y variable 
        x = sidelength*(np.sin(theta)) + point_x
        y = sidelength*(np.cos(theta)) + point_y
        
        
        # state a conditional statements on loop in even numbers
        if a % 2 == 0:
            x = sidelength*(np.sin(theta))*(-1) + point_x
            y = sidelength*(np.cos(theta))*(-1) + point_y
        
        # put all of the output to coor_list variable
        coor_list.append((x,y))

    # convert coor_list into array
    coord = np.array(coor_list)
        
    # calculate area and plot hexagon with coord variable
    area = (np.sqrt(3)/2)*(sidelength**2)
    hexagon = sg.Polygon(coord)
    return hexagon

# grid generator function
def grid_hex(type, point_init, sidelength):
    '''
    function to generate hexagon shape grid
    Parameter:
    - s: (int) side length of the hexagon shape
    - point_init: (shapely point list) consist of x, y as an initial point placed at center
    - type: (string) the style of hexagon, which is between vertical and horizontal

    Return:
    - hex_grid: (shape object) an output of shapely geometry
    '''
    if type not in ["vertical", "horizontal"]:
        raise TypeError("type of hexagon invalid! must be either vertical or horizontal")
    hex_grid = []

    # initiate first state of integer variable for looping purposes
    # do the loop for coordinate plotting
    for point in point_init:
        point_x = point.x
        point_y = point.y
        if type == "vertical":
            hexagon = hex_v (sidelength, x_init = point_x, y_init = point_y)
        
        if type == "horizontal":
            hexagon = hex_v (sidelength, x_init = point_x, y_init = point_y)
        
        hex_grid.append(hexagon)

    return hex_grid

def export_to_shapefile(target, filename, crs):
    """
    Converts a list of Shapely Point objects to a GeoDataFrame and exports it as a shapefile.
    
    Parameters:
        point_sequence (list): List of Shapely Point objects.
        filename (str): The output shapefile name (e.g., "points.shp").
        crs (int, optional): Coordinate Reference System (we will use 32748 for this occasion).
    """
    # Create a dictionary for the GeoDataFrame
    gdf = gpd.GeoDataFrame({"geometry": target})
    gdf = gdf.set_crs(crs)

    # export GeoDataFrame object into shapefile
    gdf = gdf.to_file(filename)
    
    return gdf