MorseCode = {
    "a": "._", "b": "_...", "c": "_._.", "d": "_..", "e": ".", "f": ".._.", "g": "__.",
    "h": "....", "i": "..", "j": ".___", "k": "_._", "l": "._..", "m": "__", "n": "_.", "o": "___", "p": ".__.",
    "q": "__._", "r": "._.", "s": "...", "t": "_", "u": ".._", "v": "..._", "w": ".__", "x": "_.._", "y": "_.__",
    "z": "__..", "1": ".____", "2": "..___", "3": "...__", "4": "...._", "5": ".....", "6": "_....", "7": "__...",
    "8": "___..", "9": "____.", "0": "_____", "?": "..__..", "!": "_._.__", ".": "._._._", ",": "__..__", ";": "_._._.",
    ":": "___...", "+": "._._.", "-": "_...._", "/": "_.._.", "=": "_..._",
}

print("Welcome to the Morse Code Converter from Text.")
flag = True

while flag:
    print("\n1.Enter the code\t 2.Exit")
    print("Please enter your choice: ")
    choice = input()
    if choice == "1":
        print("Please enter the string: ")
        string = input()
        string = string.lower()
        morse_code = ""
        for char in string:
            if char not in MorseCode:
                print("Morse Code not possible")
                break;
            else:
                morse_code += MorseCode[char]
        if morse_code != "":
            print(f"The Morse Code for the given string is: {morse_code}")
    elif choice == "2":
        print("Thank you!😊")
        flag = False
    else:
        print("Please enter the valid choice.☹️")
