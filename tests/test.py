def calculate_total(products):
    total = 0
    for product in products:
        total += product['price']
    return total

def test_calculate_total_with_empty_list():
    assert calculate_total([]) == 0

def test_calculate_total_with_single_product():
    products = [
        {
            "name":"Notebook",
            "price":5
        }
    ]
    assert calculate_total(products) == 5

def test_calculate_total_with_multiple_product():
    products = [
        {
            "name":"Notebook",
            "price":2500
        },
        {
            "name":"tablet",
            "price":1000
        },
        {
            "name":"Descktop",
            "price":5500
        },
        {
            "name":"mousepad",
            "price":60
        }
    ]
    assert calculate_total(products) == 9060


if __name__ == '__main__':
    test_calculate_total_with_empty_list()
    test_calculate_total_with_single_product()
    test_calculate_total_with_multiple_product()