def calculate_structure_sum(*args):
    sum_elements = 0
    print(args)
    data = args[0]
    for i in data:
        print(i)
        first = i
        if isinstance(i, str):
            sum_elements += len(i)
        if isinstance(first, list):
            for i in first:
                if isinstance(i, str):
                    sum_elements += len(i)
                elif isinstance(i, int):
                    sum_elements += i

        if isinstance(first, dict):
            for item in first.values():
                sum_elements += item
            for item in first.keys():
                sum_elements += len(item)

        if isinstance(first, tuple):
            for item in first:
                print(item)
                if isinstance(item, tuple):
                    if len(item) == 0:
                        continue
                if isinstance(item, int):
                    sum_elements += item
                if isinstance(item, dict):
                    for i in item.values():
                        sum_elements += i
                    for i in item.keys():
                        sum_elements += len(i)
                if isinstance(item, list):
                    for i in item:
                        print(i)
                        if isinstance(i, str):
                            sum_elements += len(i)
                        if isinstance(i, int):
                            sum_elements += i
                        if isinstance(i, dict):
                            print(i)
                            i = i[0]
                            print('            ', i)
                            if isinstance(i, tuple):
                                for j in i:
                                    if isinstance(j, int):
                                        sum_elements += j
                                    if isinstance(j, str):
                                        sum_elements += len(j)



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