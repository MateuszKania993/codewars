from collections import Counter


def rot(strng):
    lista = strng.split('\n')
    print(lista)
    string = ''
    for element in lista[::-1]:
        string += f"{element[::-1]}\n"
    string, rest = string[:-1], string[-1:]
    return repr(string)


def selfie_and_rot(strng):
    lista = strng.split('\n')
    string = ''
    for element in lista:
        string += f"{element}....\n"
    for element in lista[::-1]:
        string += f"....{element[::-1]}\n"
    string, rest = string[:-1], string[-1:]
    return repr(string)


# your code
def oper(fct, s):
    return fct(s)


print(oper(rot, "fijuoo\nCqYVct\nDrPmMJ\nerfpBA\nkWjFUG\nCVUfyL"))
print(oper(selfie_and_rot, "fijuoo\nCqYVct\nDrPmMJ\nerfpBA\nkWjFUG\nCVUfyL"))


def count(string):
    if not string:
        return {}
    else:
        result = {}
        a = Counter(string)
        for i, j in a.items():
            result[i] = j
        print(result)
    return result


print(count('aba'))


def new_string(string):
    return f'{string[-1]}{string[1:-1]}{string[0]}'


print(new_string("abcdef"))

for number in range(1, 51):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

print("Enter text:")
text = input()


def len_count(text):
    len = 0
    for letter in text:
        len += 1
    return len


print(len_count(text))