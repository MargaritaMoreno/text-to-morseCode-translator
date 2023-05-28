abc = {
   'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'
    } 

print("Welcome to the morse code translator")
user_input = input("Please enter your word: ").upper()
user = list(user_input)

morse_word = []
for word in user:
    if word in abc.keys():
       new_letter = abc[word]
       morse_word.append(new_letter) 
    else:
        print("Invalid input")   
converted_word = "".join(morse_word)  
print(f"The morse code for {user_input} is: {converted_word}")