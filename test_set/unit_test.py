import os
import pytest
import numpy as np
from shapely.geometry import Point
import sys
sys.path.append(os.path.abspath("/home/ziad_bwdn/hex_grid/src"))
import utils
from utils import init_rhomb_seq  # Replace with actual module name

def test_output_type():
    """Test if the function returns a list of Point objects."""
    result = init_rhomb_seq([0, 0], 10, 3)
    assert isinstance(result, list)
    assert all(isinstance(pt, Point) for pt in result)

def test_output_not_empty():
    """Test that the function returns a non-empty list when cols > 0 and sidelength > 0."""
    result = init_rhomb_seq([0, 0], 10, 3)
    assert len(result) > 0

def test_invalid_sidelength():
    """Test that the function raises an error if sidelength is not greater than zero."""
    with pytest.raises(ValueError):
        init_rhomb_seq([0, 0], 0, 3)  # Invalid sidelength
        
def test_one_column():
    """Test the function with cols = 1, which should return at least one point."""
    result = init_rhomb_seq([0, 0], 10, 1)
    assert len(result) > 0

def test_symmetry():
    """Check if points are symmetrically generated around the origin."""
    result = init_rhomb_seq([0, 0], 10, 3)
    for point in result:
        reflected_point = Point(-point.x, -point.y)
        assert reflected_point in result  # Ensure symmetry exists

if __name__ == "__main__":
    pytest.main()