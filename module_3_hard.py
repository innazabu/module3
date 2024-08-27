def calculate_structure_sum(data):
    sum_elements = 0
    if isinstance(data, int):
        return data
    elif isinstance(data, str):
        return len(data)
    elif isinstance(data, (list, tuple, set)):
        for element in data:
            sum_elements += calculate_structure_sum(element)
    elif isinstance(data, dict):
        for key, value in data.items():
            sum_elements += calculate_structure_sum(key)
            sum_elements += calculate_structure_sum(value)
    return sum_elements


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print('Ответ: ', result)
