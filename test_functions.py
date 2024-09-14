import pytest
from patient_equations import map_calc, co_fick_calc, sv_calc 

# Test cases for map_calc function
def test_map_calc_typical():
    assert map_calc(120, 80) == 93  # Expected result for typical values

def test_map_calc_zero_input():
    assert map_calc(0, 0) == 0  # Expected result for both inputs being zero

def test_map_calc_high_values():
    assert map_calc(200, 180) == 187  # Expected result for high values

def test_co_fick_calc_age_gt_70():
    age = 75
    bsa = 1.8
    SaO2 = 95
    SvO2 = 80
    hgb = 15
    expected_result = 6.57  # The expected result for these input values
    assert co_fick_calc(age, bsa, SaO2, SvO2, hgb) == expected_result

def test_co_fick_calc_age_lt_70():
    age = 60
    bsa = 2.0
    SaO2 = 98
    SvO2 = 85
    hgb = 16
    expected_result = 8.97 # The expected result for these input values
    assert co_fick_calc(age, bsa, SaO2, SvO2, hgb) == expected_result
    
def test_sv_calc_typical():
    # Typical values for cardiac output (co) and heart rate (hr)
    co = 5.7
    hr = 75
    expected_result = 76  # The expected result for these input values
    assert sv_calc(co, hr) == expected_result

def test_sv_calc_zero_input():
    # Zero cardiac output (co) should result in zero stroke volume (sv)
    co = 0
    hr = 80
    assert sv_calc(co, hr) == 0

def test_sv_calc_float_values():
    # Test with float values for cardiac output (co) and heart rate (hr)
    co = 4.8
    hr = 68.5
    expected_result = 70  # The expected result for these input values
    assert sv_calc(co, hr) == expected_result
    
if __name__ == "__main__":
    pytest.main()