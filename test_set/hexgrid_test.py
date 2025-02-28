import os
import pytest
from shapely.geometry import Point
import sys
sys.path.append(os.path.abspath("/home/ziad_bwdn/hex_grid/src"))
import utils
from utils import grid_hex

# Define a dummy hex_v function that simply returns a dictionary
# capturing the inputs. This helps us verify that grid_hex is calling it correctly.
def dummy_hex_v(sidelength, x_init, y_init):
    return {"sidelength": sidelength, "x": x_init, "y": y_init}

# Automatically patch hex_v in grid_module with dummy_hex_v for all tests in this file.
@pytest.fixture(autouse=True)
def patch_hex_v(monkeypatch):
    # Patch the hex_v function in the grid_module namespace.
    monkeypatch.setattr(utils, "hex_v", dummy_hex_v)

def test_grid_hex_vertical():
    # Create a list of shapely Points.
    points = [Point(1, 2), Point(3, 4)]
    sidelength = 5
    # Call grid_hex with type "vertical"
    result = grid_hex("vertical", points, sidelength)
    
    # For each point, the dummy_hex_v should have returned a dict with the given sidelength, x and y.
    expected = [{"sidelength": sidelength, "x": p.x, "y": p.y} for p in points]
    assert result == expected

def test_grid_hex_horizontal():
    # Create a list with a single shapely Point.
    points = [Point(10, 20)]
    sidelength = 7
    # Call grid_hex with type "horizontal"
    result = grid_hex("horizontal", points, sidelength)
    
    expected = [{"sidelength": sidelength, "x": points[0].x, "y": points[0].y}]
    assert result == expected

def test_invalid_type():
    # If the type is not "vertical" or "horizontal", a TypeError should be raised.
    points = [Point(0, 0)]
    with pytest.raises(TypeError):
        grid_hex("diagonal", points, 3)
