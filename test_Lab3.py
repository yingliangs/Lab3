import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [1,2,6,5]
    test_arr = [1,2,5,6]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [1,2,6,5]
    test_arr = [6,5,2,1]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_too_many_n():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90,0,0,0,0,0,0,0]

    result = Lab3.bubble_sort(input_arr,Lab3.SORT_ASCENDING )

    assert (result == 1)

def test_bubble_sort_0():
    result = []
    input_arr = []

    result = Lab3.bubble_sort(input_arr,Lab3.SORT_DESCENDING )

    assert (result == [])

def test_bubble_sort_not_integer():
    result = []
    input_arr = [1.1]

    result = Lab3.bubble_sort(input_arr,Lab3.SORT_ASCENDING )

    assert (result == 2)