import bmi as bmi

print("Test bmi")

def test_bmi_under_weight():
    assert bmi(17.0) == -1  # BMI < 18.5

def test_bmi_normal_weight():
    assert bmi(22.0) == 0  # 18.5 <= BMI <= 25.0

def test_bmi_over_weight():
    assert bmi(27.0) == 1  # BMI > 25.0