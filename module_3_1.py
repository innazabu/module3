calls = 0
def count_calls():
    global calls
    return calls+1
def string_info(string):
    calls = count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    calls=count_calls()

    string = string.lower()

    for i in range(len(list_to_search)):
         list_to_search[i] = list_to_search[i].lower()

    if string in list_to_search:
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
