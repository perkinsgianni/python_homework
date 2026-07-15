# Task 1: Diary

import traceback

try:
    with open('diary.txt', 'a') as file:
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
    print(f"An exception occurred. {type(e).__name__}")

    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')

    print(f"Stack trace: {stack_trace}")