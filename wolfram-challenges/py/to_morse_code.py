
# Problem: https://challenges.wolframcloud.com/challenge/write-in-morse-code
# Resources: https://en.wikipedia.org/wiki/Morse_code

MORSEALPHABET = {
    "a": ".-", 
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--.."
}

def to_morse_code(text):
    morse_code = ''
    for char in text:
        if char == ' ':
            morse_code += ' /'
            continue

        if char in ",.'":
            morse_code += f' {char}'
            continue

        c = char.lower()
        code = MORSEALPHABET[c]
        morse_code += f" {code}"
    return morse_code


if __name__ == '__main__':
    text = "When in the Course of human events, it becomes necessary  for one people to dissolve the political bands which have connected  them with another, and to assume, among the Powers of the earth, the  separate and equal station to which the Laws of Nature and of  Nature's God entitle them, a decent respect to the opinions of  mankind requires that they should declare the causes which impel them  to the separation."
    res = to_morse_code(text)
    print(res)