import pytest
from my_proj.sum_func import add, add_positive

# Test case for adding different data types, expecting TypeError
def test_add_diff_data_types():
    with pytest.raises(TypeError):
        add('d', 5) 

# Test case for adding two positive numbers
def test_add():
    assert add(2, 3) == 5

# Test case for add_positive where both numbers are positive
def test_add_both_positive():
    assert add_positive(5, 1) == 6

# Test case for add_positive where both numbers are zero, expecting None
def test_add_both_zero():
    assert add_positive(0, 0) == None

# Test case for add_positive where the first number is zero, expecting None
def test_add_a_zero():
    assert add_positive(0, 5) == None

# Test case for add_positive where the second number is zero, expecting None
def test_add_b_zero():
    assert add_positive(5, 0) == None

# Test case for add_positive where both numbers are negative, expecting None
def test_add_both_negative():
    assert add_positive(-5, -6) == None

# Test case for add_positive where the first number is negative, expecting None
def test_add_a_negative():
    assert add_positive(-5, 55) == None

# Test case for add_positive where the second number is negative, expecting None
def test_add_b_negative():
    assert add_positive(5, -10) == None