# Task 1: Hello

# Write a hello function that takes no arguments and returns Hello!.  Now, what matters here is what the function returns.  You can print() whatever you want for debugging purposes, but the tests ignore that, and only check the return value.

def hello():
    return "Hello!"

print("Task 1:", hello())

#//////////////////////////////////////

# Task 2: Greet with a Formatted String

# Write a greet function.  It takes one argument, a name, and returns Hello, Name!.  Use a formatted string.  Note that you have to return exactly the right string or the test fails -- but PyTest tells you what didn't match.

def greet(name):
    return "Hello, " + name + "!"

print("Task 2:", greet("Gianni"))
print("Task 2:", greet("Kim"))

#//////////////////////////////////////

# Task 3: Calculator

# Write a calc function. It takes three arguments. The default value for the third argument is "multiply". The first two arguments are values that are to be combined using the operation requested by the third argument, a string that is one of the following add, subtract, multiply, divide, modulo, int_divide (for integer division) and power. The function returns the result.
# Error handling: When the function is called, it could ask you to divide by 0. That will throw an exception: Which one? You can find out by triggering the exception in your program or in the Python Interactive Shell. Wrap the code within the calc function in a try block, and put in an except statement for this exception. If the exception occurs, return the string "You can't divide by 0!".
# More error handling: When the function is called, the parameters that are passed might not work for the operation. For example, you can't multiply two strings. Find out which exception occurs, catch it, and return the string "You can't multiply those values!".
# Tip: You have to do different things for add, multiply, divide and so on. So you can do a conditional cascade, if/elif/elif/else. That's perfectly valid. But you might want to use the match-case Python statement instead.
# Again, as you complete each function, you run the test to see whether everything is correct.

def calc(num1, num2, operation="multiply"):
    try: 
        match operation:
            case "add":
                return num1 + num2
            case "subtract":
                return num1 - num2
            case "multiply":
                return num1 * num2
            case "divide":
                return num1 / num2
            case "modulo":
                return num1 % num2
            case "int_divide":
                return num1 // num2
            case "power":
                return num1 ** num2
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"

print("Task 3:", calc(1, 2, "add"))
print("Task 3:", calc(1, 2, "subtract"))
print("Task 3:", calc(1, 2, "multiply"))
print("Task 3:", calc(1, 2, "divide"))
print("Task 3:", calc(1, 2, "modulo"))
print("Task 3:", calc(1, 2, "int_divide"))
print("Task 3:", calc(1, 2, "power"))

#//////////////////////////////////////

# Task 4: Data Type Conversion

# Create a function called data_type_conversion. It takes two parameters, the value and the name of the data type requested, one of float, str, or int. Return the converted value.
# Error handling: The function might be called with a bad parameter. For example, the caller might try to convert the string "nonsense" to a float. Catch the error that occurs in this case. If this error occurs, return the string You can't convert {value} into a {type}., except you use the value and data type that are passed as parameters -- so again you use a formatted string.

def data_type_conversion(num, data_type):
    try:
        match data_type:
            case "float":
                return float(num)
            case "str":
                return str(num)
            case "int":
                return int(num)
    except ValueError:
        return "You can't convert " + num + " into a " + data_type + "."

print("Task 4:", data_type_conversion(1, "float"))
print("Task 4:", data_type_conversion(2, "str"))
print("Task 4:", data_type_conversion(3, "int"))

#//////////////////////////////////////

# Task 5: Grading System, Using *args

# Create a grade function. It should collect an arbitrary number of parameters, compute the average, and return the grade. based on the following scale, popular in American schools:
# A: 90 and above
# B: 80-89
# C: 70-79
# D: 60-69
# F: Below 60
# When you use *args you get access to a variable named args in your function, which is a tuple, an ordered collection of values like a list. You'll learn more about tuples and lists in the next lesson. There are some helpful functions you can use at this point: sum(args), len(args), and so on. One of the curiosities of Python is that these are not methods of any class. They are standalone functions.
# Handle the error that occurs if the parameters are nonsense. Return the string "Invalid data was provided." in this case. (Typically, you don't handle every possible exception in your error handling, except if the values in the parameters come from the end user.)

def grade(*args):
    try:
        average = sum(args) / len(args)

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except TypeError:
        return "Invalid data was provided."

print("Task 5:", grade(81, 32, 53, 74))

#//////////////////////////////////////

# Task 6: Use a For Loop with a Range

# Create a function called repeat. It takes two parameters, a string and a count, and returns a new string that is the old one repeated count times.
# You could return string * count to pass the test — but for this task, use a for loop and a range.

def repeat(str, count):
    newStr = ''

    for i in range(count):
        newStr += str
        # print(newStr)
    
    return newStr

print("Task 6:", repeat("Hey", 5))

# Task 7: Student Scores, Using **kwargs

# Create a function called student_scores. It takes one positional parameter and an arbitrary number of keyword parameters. The positional parameter is either "best" or "mean". If it is "best", the name of the student with the highest score is returned. If it is "mean", the average score is returned.
# As you are using **kwargs, your function can access a variable named kwargs, which is a dict. The next lesson explains about dicts. What you need to know now is the following:
# A dict is a collection of key value pairs.
# You can iterate through the dict as follows:
# for key, value in kwargs.items():
# You can also get kwargs.keys() and kwargs.values().
# The arbitrary list of keyword arguments uses the names of students as the keywords and their test score as the value for each.

def student_scores(positional, **kwargs):
    if positional == "best":
        return max(kwargs, key=kwargs.get)
    elif positional == "mean":
        return sum(kwargs.values()) / len(kwargs.values())

    
print("Task 7:", student_scores("best", Gianni=95, Blair=88, Serena=97))
print("Task 7:", student_scores("mean", Gianni=95, Blair=88, Serena=97))

#//////////////////////////////////////

# Task 8: Titleize, with String and List Operations

# Create a function called titleize. It accepts one parameter, a string. The function returns a new string, where the parameter string is capitalized as if it were a book title.
# The rules for title capitalization are: (1) The first word is always capitalized. (2) The last word is always capitalized. (3) All the other words are capitalized, except little words. For the purposes of this task, the little words are "a", "on", "an", "the", "of", "and", "is", and "in".
# The following string methods may be helpful: split(), join(), and capitalize().
# The split() method returns a list. You might store this in the words variable.  words[-1] gives the last element in the list.
# The in comparison operator: You have seen in used in loops. But it can also be used for comparisons, for example to check to see if a substring occurs in a string, or a value occurs in a list.
# Useful pattern: As you loop through the words in the words list, it is helpful to have the index of the word for each iteration. You can access that index using the enumerate() function:
# for i, word in enumerate(words):

def titleize(str):
    words = str.split(" ")
    # print(words)
    little_words = "a", "on", "an", "the", "of", "and", "is", "in"
    # print(little_words)
    newStr = []

    for i, word in enumerate(words):
        # print(i, word)
        if i == 0 or i == len(words) - 1 or word not in little_words:
            # print("Word is not a little word")
            word = word.capitalize()
            # print(word)
            newStr.append(word)
            # print(newStr)
        else:
            newStr.append(word)
            # print(newStr)

    return " ".join(newStr) # join words into str separated by space

print("Task 8:", titleize("all i want is everything"))

#//////////////////////////////////////

# Task 9: Hangman, with more String Operations

# Create a function hangman. It takes two parameters, both strings, the secret and the guess.
# The secret is some word that the caller doesn't know. So the caller guesses various letters, which are the ones in the guess string.
# A string is returned. Each letter in the returned string corresponds to a letter in the secret, except any letters that are not in the guess string are replaced with an underscore. The others are returned in place. Not everyone has played this kid's game, but it's common in the US.
# Example: Suppose the secret is "alphabet" and the guess is "ab". The returned string would be "a___ab__".
# Note that Python strings are immutable. That means that the following code would give an error:
# secret = "alphabet"
# secret[1] = "_"
# On the other hand, you can concatenate strings with the + operator.

def hangman(secret, guess):
    str = []

    for letter in secret:
        # print(letter)
        if letter in guess:
            str.append(letter)
            # print(str)
        else:
            str.append("_")
            # print(str)

    return "".join(str)

print("Task 9:", hangman("dream", "rgnreijg"))
print("Task 9:", hangman("love", "ejfhes"))

#//////////////////////////////////////

# Task 10: Pig Latin, Another String Manipulation Exercise

# Pig Latin is a kid's trick language. Each word is modified according to the following rules. (1) If the string starts with a vowel (aeiou), "ay" is tacked onto the end. (2) If the string starts with one or several consonants, they are moved to the end and "ay" is tacked on after them. (3) "qu" is a special case, as both of them get moved to the end of the word, as if they were one consonant letter.
# Create a function called pig_latin. It takes an English string or sentence and converts it to Pig Latin, returning the result. We will assume that there is no punctuation and that everything is lower case.

def pig_latin(str):
    vowels = "aeiouAEIOU"
    words = str.split()
    result = []

    for word in words:
        if word[0] in vowels:
            result.append(word + "ay")
            continue

        for i, letter in enumerate(word):
            if letter in vowels:
                if "qu" in word[:i+1]: # if substr up to curr vowel contains qu
                    # print(word[i+1:] + word[:i+1] + "ay")
                    result.append(word[i+1:] + word[:i+1] + "ay") # add substr after vowel to substr up to and including vowel
                else:    
                    # print(word[i:], word[:i])
                    result.append(word[i:] + word[:i] + "ay") # add substr starting from vowel to substr before vowel
                break

    return " ".join(result)

print("Task 10:", pig_latin("live"))
print("Task 10:", pig_latin("alive"))
print("Task 10:", pig_latin("quiet"))
print("Task 10:", pig_latin("square"))