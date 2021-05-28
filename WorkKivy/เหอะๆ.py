alphabet = [chr(i) for i in range(65, 92)]
wtf_code = '112,212,222,222,221,2,221,1121,5353,355,96,9696,969,6669,778,887,8,878,887,778'.split(
    ',')
num_code = [[int(j) for j in i]for i in wtf_code]
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}
MORSE_CODE_DICT = {value: key for (key, value) in MORSE_CODE_DICT.items()}
morse = []
for i in num_code:
    a = ''.join(map(str, i))
    a = a.replace(str(max(i)), '-')
    a = a.replace(str(min(i)), '.')
    morse.append(a)
correct_morse = list(map(lambda s: MORSE_CODE_DICT[s], morse))
correct_morse = [alphabet[alphabet.index(i)-2] for i in correct_morse]
print('Answer is\n'+''.join(correct_morse))
