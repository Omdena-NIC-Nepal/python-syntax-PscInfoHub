def format_string(name, age):
    return f"My name is {name} and I am {age} years old"

def conditional_check(number):
    if number > 10:
        return "Greater"
    elif number < 10:
        return "Lesser"
    else:
        return "Equal"

def loop_sum(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

def list_operations(numbers):
    return sum(numbers), max(numbers), min(numbers)

def dict_operations(students_dict):
    return [name for name, score in students_dict.items() if score > 80]

def set_operations(list1, list2):
    return set(list1).intersection(set(list2))

def arithmetic_ops(a, b):
    return {
        "sum": a+b,
        "difference": a-b,
        "product": a*b,
        "quotient": a/b if b != 0 else None
        }

def logical_ops(x, y):
    return {
        "and": x and y,
        "or": x or y,
        "not_x": not x
    }

def bitwise_ops(a, b):
    return {
        "and": a&b,
        "or": a|b,
        "xor": a^b
    }