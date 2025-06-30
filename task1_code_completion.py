# Task 1: Sort list of dictionaries by a key

# Manual Implementation
def sort_dicts_by_key(data, sort_key):
    return sorted(data, key=lambda x: x[sort_key])

# AI-Suggested Implementation (GitHub Copilot)
def sort_dict_list(dict_list, key):
    dict_list.sort(key=lambda d: d[key])
    return dict_list

# Sample usage
data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
print(sort_dicts_by_key(data, 'age'))
print(sort_dict_list(data, 'age'))
