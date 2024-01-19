def test_root_no_found(client):
    """Функция проверки на несуществующую страницу"""
    response = client.get("/");

    assert response.status_code == 404


def binary_serch(array, value):
    low = 0;
    high = len(array) - 1

    while low <= high:
        mid = (low + high) / 2
        mid_value = array[mid]
        if mid_value == value:
            return mid
        if mid_value > value:
            high = mid - 1
        else:
            low = mid + 1
    return -1


print(
  binary_serch(list(range(0, 100)), 13)
)
