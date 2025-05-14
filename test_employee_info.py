from employee_info import calculate_average_salary, get_employees_by_age_range, get_employees_by_dept


def test_age():
    expected = [{"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
                {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},]
    result = get_employees_by_age_range(2,30)
    assert(expected == result)


def test_salary():
    expected =  60166.666666666664
    result = calculate_average_salary()
    assert(expected == result)
def test_employee_dept():
    expected = [{"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},]
    result = get_employees_by_dept('Marketing')
    assert(expected == result)