def delVowel(inp):
    vowel = ['a','i','u','e','o', ' ']
    outp = ""

    for character in inp:
        if character.lower() not in vowel:
            outp += character
    return outp
print(delVowel("Nurul Fikri"))