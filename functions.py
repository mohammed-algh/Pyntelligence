# this file contains functions that will be used in different places

#create a exception for ending input_long_str function
class EndText(Exception):
    "Raised whan the input was empty for 5 lines"
    pass

#function to read more than one line from user
def input_long_str(text = "") -> str:
    all_text =""
    if text != "":
        print(text, end=" ")
    print("Enter 'C^' to stop input function")
    while True:
        try:
            line = input()
            if "C^" in line:
                all_text += line.replace("C^","") + "\n"
                raise EndText
        except EndText:
            break
        all_text += line + "\n"
    return all_text
