############################################
## BRAILLE CONVERSION CODE IMPORTED FROM NAPAT AND YUWARIN's FILE
## Program separated into 4 main parts:
## 1. Check the input
## 2. Convert the input into Braille
## 3. Write the output into a text file
## 4. Driver code to run the conversion
##
## To import the code, use the following code:
## from helperFunctions.brailleConversion import run_braille_conversion
############################################

##---------------BRAILLE CONVERSION STARTS HERE---------------##
letters = (
    list("ABCDEFGHIJKLMNOPQRSTUVWXYZ") +
    list("abcdefghijklmnopqrstuvwxyz") +
    list("1234567890") +
    [',', ';', ':', '.', '!', '(', ')', '‘', '’', '“', '”', '?', '/', '#', '\'', '-', '‒', '–', '—', '―', ' ']
)

upper_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("1234567890")
num_lower_letters = list("abcdefghij")
dict_letters = {'A': chr(10241), 'B': chr(10243), 'C': chr(10249), 'D': chr(10265), 'E': chr(10257), 'F': chr(10251),
               'G': chr(10267), 'H': chr(10259), 'I': chr(10250), 'J': chr(10266), 'K': chr(10245), 'L': chr(10247),
               'M': chr(10253), 'N': chr(10269), 'O': chr(10261), 'P': chr(10255), 'Q': chr(10271), 'R': chr(10263),
               'S': chr(10254), 'T': chr(10270), 'U': chr(10277), 'V': chr(10279), 'W': chr(10298), 'X': chr(10285),
               'Y': chr(10301), 'Z': chr(10293), 'a': chr(10241), 'b': chr(10243), 'c': chr(10249), 'd': chr(10265),
               'e': chr(10257), 'f': chr(10251), 'g': chr(10267), 'h': chr(10259), 'i': chr(10250), 'j': chr(10266),
               'k': chr(10245), 'l': chr(10247), 'm': chr(10253), 'n': chr(10269), 'o': chr(10261), 'p': chr(10255),
               'q': chr(10271), 'r': chr(10263), 's': chr(10254), 't': chr(10270), 'u': chr(10277), 'v': chr(10279),
               'w': chr(10298), 'x': chr(10285), 'y': chr(10301), 'z': chr(10293), '1': chr(10241), '2': chr(10243),
               '3': chr(10249), '4': chr(10265), '5': chr(10257), '6': chr(10251), '7': chr(10267), '8': chr(10259),
               '9': chr(10250), '0': chr(10266), ',': chr(10242), ';': chr(10246), ':': chr(10258), '.': chr(10290),
               '!': chr(10262), '(': chr(10294), ')': chr(10294), '‘': chr(10278), '’': chr(10292), '“': chr(10278),
               '”': chr(10292), '?': chr(10278), '/': chr(10252), '#': chr(10300), '\'': chr(10244), '’': chr(10244),
               '­': chr(10276), '-': chr(10276), '‐': chr(10276), '‑': chr(10276), '‒': chr(10276), '–': chr(10276),
               '—': chr(10276), '―': chr(10276), ' ': ' '}

## Checking Letters
def Check(testcase):
    new_testcase = []
    for i in testcase:
        if i not in letters:
            print("Input is invalid.")
            new_testcase = []
            return new_testcase
        new_testcase.append(i)
    # print(new_testcase)
    return new_testcase
    
def DictCheck(testcase):
    new_testcase = []
    mode_numbers = 0
    for i in testcase:
        if i in upper_letters:
            new_testcase.append(chr(10272))
        if i in numbers and mode_numbers == 0:
            mode_numbers = 1
            new_testcase.append(chr(10300))
        elif i in num_lower_letters and mode_numbers == 1:
            mode_numbers = 0
            new_testcase.append(chr(10288))
        else:
            mode_numbers = 0
        i = dict_letters[i]
        new_testcase.append(i)
    # print(new_testcase)
    for i in new_testcase:
        print(i, end='')
    print('')
    return new_testcase

##---------------BRAILLE CONVERSION ENDS HERE---------------##

##---------------WRITING OUTPUT STARTS HERE---------------##

def writing_output(filename, elements):
    # Constants for text wrapping (approximately 80 characters per line for A4 with 12pt font)
    max_chars_per_line = 80
    text = "".join(elements)

    with open(filename, "w", encoding="utf-8") as file:
        words = text.split()
        current_line = ""

        for word in words:
            if len(current_line) + len(word) + 1 <= max_chars_per_line:
                current_line += (word + " ") if current_line else word
            else:
                file.write(current_line.rstrip() + "\n")
                current_line = word

        if current_line:
            file.write(current_line.rstrip() + "\n")

    print(f"File '{filename}' created successfully!")

##---------------WRITING OUTPUT ENDS HERE---------------##


##---------------DRIVER CODE STARTS HERE---------------##
def run_braille_conversion(text, output_file):
    ListText = []
    for i in text:
        ListText.append(i) #change the original text from ['abcd'] to ['a','b','c','d'].
    outputBraille = DictCheck(ListText) #conversion
    writing_output(output_file, outputBraille) #wrting the output into txt file
    return
