def pangrams(s):
    # Write your code here
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    arrOfLetters = []
    for char in s:
        if str.lower(char) not in arrOfLetters and str.lower(char) in alphabet:
            arrOfLetters.append(str.lower(char))
    if len(arrOfLetters) == 26:
        return "pangram"
    else:
        return "not pangram"
