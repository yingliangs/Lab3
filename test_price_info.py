from price_info import total_cost_shopping, cost_of_fruits

test_price_list = {'apple':1.50,'orange':1.30,'papaya':2.0}
test_quantity = {'apple':10, 'orange':2, 'papaya':7}
def test_total_cost():
    
    expected = 46.75
    total_cost = total_cost_shopping() 

    assert (total_cost == expected)


def test_cost_fruits():

    expected = 8.4
    result = cost_of_fruits('apple', 7)

    assert(expected == result)