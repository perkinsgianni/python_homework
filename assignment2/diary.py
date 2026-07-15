# Task 1: Diary

# Create a program called diary.py. Add code to do the following:
# Open a file called diary.txt for appending.
# In a loop, prompt the user for a line of input. The first prompt should say, "What happened today? ". All subsequent prompts should say "What else? "
# As each line is received, write it to diary.txt, with a newline (\n) at the end.
# When the special line "done for now" is received, write that to diary.txt. Then close the file and exit the program (you just exit the loop).
# Wrap all of this in a try block. If an exception occurs, catch the exception and print out "An exception occurred." followed by the name of the exception itself. Now, normally, you catch specific types of exceptions, and handle each according to program logic. In this case, you can catch any non-fatal exceptions via an except for Exception, and then display the information from the exception and exit the program. The traceback module provides a way to include function traceback information in your error message, which will make it easier to find the error. You can use the following code to handle exceptions using the traceback module.
# Open the file using a with statement (inside the try block), and rely on that statement to handle the file close.
# The input statement should be inside the loop inside the with block.

try:
    with open('assignment2/diary.txt', 'a') as file:
        # first prompt
        prompt = "What happened today? "
        
        while True:
            # get answer to prompt from user, write to file
            line = input(prompt)
            file.write(line + "\n")

            # check for special line to exit loop
            if line.lower() == "done for now":
                break

            # subsequent prompts
            prompt = "What else? "
except Exception as e:
    print(f"An exception error occurred: {e}")