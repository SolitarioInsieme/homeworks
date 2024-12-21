def count_calls():
    global calls
    calls += 1
    return calls
def string_info(string):
    count_calls()
    string_modefied = (len(string), string.upper(), string.lower())
    return string_modefied
def is_contains(string, list_to_search):
    count_calls()
    for element in range(len(list_to_search)):
        if type(list_to_search[element]) == str:
            if list_to_search[element].lower() == string.lower():
                return True
    return False
calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print('Функции были вызваны ', calls, 'раз')