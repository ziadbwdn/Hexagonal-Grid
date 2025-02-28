# library importing
import os
import numpy as np
import matplotlib.pyplot as plt
import shapely.geometry as sg
import geopandas as gpd
from shapely.geometry import shape
from shapely.geometry import Point

import sys
sys.path.append(os.path.abspath("/home/ziad_bwdn/hex_grid/src"))
import utils

# import shapefile and extract centroid from shape
AOI = gpd.read_file("/home/ziad_bwdn/hex_grid/data/raw/AOI.shp")
AOI['centroid'] = AOI.geometry.centroid
x_values = AOI.geometry.centroid.x.tolist()
y_values = AOI.geometry.centroid.y.tolist()

# declare variable needed for the parameter
point_init = [x_values[0], y_values[0]]
sidelength = 1000
cols = 5
rows = 4

# apply the function of generating sequences
rhomb_grid = utils.init_rhomb_seq(point_init, sidelength, cols)
rhomb_vgrid = utils.init_rhomb_seqv(point_init, sidelength, cols)
rect_grid = utils.init_rect_seq(point_init, sidelength, cols, rows)
rect_vgrid = utils.init_rect_seqv(point_init, sidelength, cols, rows)

# set the crs will be used
crs = 32748

# generate tesselated hexagonal grid
rh_hex = utils.grid_hex (type = "horizontal", point_init = rhomb_grid, sidelength = sidelength)
rh_vhex = utils.grid_hex (type = "vertical", point_init = rhomb_grid, sidelength = sidelength)
rec_hex = utils.grid_hex (type = "horizontal", point_init = rect_grid, sidelength = sidelength)
rec_vhex = utils.grid_hex (type = "vertical", point_init = rect_vgrid, sidelength = sidelength)

# export to shapefile with shapefile function
grid_list = [rh_hex, rh_vhex, rec_hex, rec_vhex]
gdf_rh_hex = utils.export_to_shapefile(target = rh_hex, 
                                       filename = f"/home/ziad_bwdn/hex_grid/data/processed/grid_rh_hex.shp", 
                                       crs=crs
                                    )
gdf_rh_vhex = utils.export_to_shapefile(target = rh_vhex, 
                                       filename = f"/home/ziad_bwdn/hex_grid/data/processed/grid_rh_vhex.shp", 
                                       crs=crs
                                    )
gdf_rh_hex = utils.export_to_shapefile(target = rec_hex, 
                                       filename = f"/home/ziad_bwdn/hex_grid/data/processed/grid_rec_hex.shp", 
                                       crs=crs
                                    )
gdf_rec_vhex = utils.export_to_shapefile(target = rec_vhex, 
                                       filename = f"/home/ziad_bwdn/hex_grid/data/processed/grid_rec_vhex.shp", 
                                       crs=crs
                                    )