#first question

def calculate_string_length (the_string):



    print (calculate_string_length('semicolon'))

#second question
def first_two_and_last_two_characters(string):

    if len(string) < 2:

        return ""

    return string[:2] + string[-2:]


print(first_two_and_last_two_characters("Afeez"))
print(first_two_and_last_two_characters("Afez"))
print(first_two_and_last_two_characters("e"))

#third question
def add_string(the_string):

    if len(the_string) < 3:

        return the_string

    if the_string.endswith('ing'):

        return the_string + 'ly'

    else:

        return the_string + 'ing'

print(add_string('jaye'))
print(add_string('kawe'))
print(add_string('un'))

#fourth question

def longest_word(the_words):

    longest = words[0]

    for word in the_words:

        if len (word) > len(longest):

            longest = word

    return longest, len(longest)

words = ["atmosphere", "puberty", "transportation", "love", "teacher", "glory"]
word, length = longest_word(words)
print(word, length)



#fifth question

def remove_odd_index(the_string):

    result = ""

    for index in range(len(the_string)):
        if index % 2 == 1:

            result += the_string[index]

    return result


print(remove_odd_index("halleluyah"))



def find_minimum(numbers):
    smallest = numbers[0]

    for number in numbers:
        if number < smallest:
            smallest = number

    return smallest


def find_maximum(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest

numbers = [180, 250,342, 500]
print(find_minimum(numbers))
print(find_maximum(numbers))

def repeat_string(string, number):
    if type(number) == float:
        return string

    return string * number

print(repeat_string("bonjour", 5))
print(repeat_string("m,aison", 3.0))

#nineth question
def square_elements(numbers):
    result = []


    for number in numbers:
        result.append(number ** 2)

    return result


numbers = [3, 5, 8, 9, 12]
print(square_elements(numbers))


#tenth question
def sum_of_square(numbers):
    total = 0

    for number in numbers:
        total += number ** 2

    return total


numbers = [3, 5, 8, 12]
print(sum_of_square(numbers))




